const fs = require('fs');
const path = require('path');
const Database = require('better-sqlite3');

function createStorage(userDataPath) {
  const root = path.join(userDataPath, 'journal');
  const backupDir = path.join(root, 'backups');
  fs.mkdirSync(backupDir, { recursive: true });

  const dbPath = path.join(root, 'trading-discipline-tracker.db');
  const db = new Database(dbPath);
  db.pragma('journal_mode = WAL');
  db.pragma('foreign_keys = ON');

  db.exec(`
    CREATE TABLE IF NOT EXISTS app_meta (
      key TEXT PRIMARY KEY,
      value TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS days (
      date TEXT PRIMARY KEY,
      payload TEXT NOT NULL,
      updated_at TEXT NOT NULL
    );
  `);

  const get = db.prepare('SELECT payload FROM days WHERE date = ?');
  const all = db.prepare('SELECT date, payload FROM days ORDER BY date');
  const upsert = db.prepare(`
    INSERT INTO days(date, payload, updated_at) VALUES(@date, @payload, @updated_at)
    ON CONFLICT(date) DO UPDATE SET payload=excluded.payload, updated_at=excluded.updated_at
  `);

  function normalize(data) {
    if (!data || typeof data !== 'object') return { version: 2, days: {} };
    const days = data.days && typeof data.days === 'object' ? data.days : data;
    return { version: 2, days };
  }

  function load() {
    const days = {};
    for (const row of all.all()) {
      try { days[row.date] = JSON.parse(row.payload); } catch (_) {}
    }
    return { version: 2, days };
  }

  function save(data) {
    const normalized = normalize(data);
    const tx = db.transaction(() => {
      for (const [date, payload] of Object.entries(normalized.days)) {
        upsert.run({ date, payload: JSON.stringify(payload), updated_at: new Date().toISOString() });
      }
    });
    tx();
    makeBackup();
    return load();
  }

  function exportJson() {
    return JSON.stringify(load(), null, 2);
  }

  function makeBackup() {
    try { db.pragma('wal_checkpoint(TRUNCATE)'); } catch (_) {}
    const stamp = new Date().toISOString().replace(/[:.]/g, '-');
    const target = path.join(backupDir, `journal-${stamp}.db`);
    fs.copyFileSync(dbPath, target);
    const files = fs.readdirSync(backupDir).sort().reverse();
    for (const file of files.slice(20)) {
      try { fs.unlinkSync(path.join(backupDir, file)); } catch (_) {}
    }
    return target;
  }

  function restore(payload) {
    const normalized = normalize(payload);
    const tx = db.transaction(() => {
      for (const [date, value] of Object.entries(normalized.days)) {
        upsert.run({ date, payload: JSON.stringify(value), updated_at: new Date().toISOString() });
      }
    });
    tx();
    makeBackup();
    return load();
  }

  function deleteDay(date) {
    if (typeof date !== 'string' || !/^[0-9]{4}-[0-9]{2}-[0-9]{2}$/.test(date)) {
      throw new Error('Invalid journal date');
    }
    // Preserve a recovery point before a user-requested deletion.
    makeBackup();
    db.prepare('DELETE FROM days WHERE date = ?').run(date);
    return { deleted: true, date };
  }


  // Merge old JSON journals into SQLite without replacing existing day records.
  // The previous desktop release stored data in:
  // <userData>/Trading Discipline Tracker/journal.json (+ rolling JSON backups).
  let legacyBaseDir = userDataPath;
  let lastLegacyReport = { filesFound: 0, filesRead: 0, daysAdded: 0, tradesAdded: 0, tradesEnriched: 0, sources: [] };

  function listLegacySources() {
    const roots = [
      path.join(userDataPath, 'Trading Discipline Tracker'),
      path.join(path.dirname(userDataPath), 'Trading Discipline Tracker'),
      path.join(path.dirname(userDataPath), path.basename(userDataPath), 'Trading Discipline Tracker')
    ];
    const files = new Set();
    for (const root of roots) {
      const mainFile = path.join(root, 'journal.json');
      if (fs.existsSync(mainFile)) files.add(mainFile);
      for (const backupFolder of [path.join(root, 'backups'), path.join(root, 'backup')]) {
        try {
          for (const name of fs.readdirSync(backupFolder)) {
            if (/^journal-.*\.json$/i.test(name) || /^.*backup.*\.json$/i.test(name)) {
              const candidate = path.join(backupFolder, name);
              if (fs.statSync(candidate).isFile()) files.add(candidate);
            }
          }
        } catch (_) {}
      }
    }
    // Process dated backups from oldest to newest, and the active journal last.
    return [...files].sort((a, b) => {
      const am = path.basename(a).toLowerCase() === 'journal.json' ? 1 : 0;
      const bm = path.basename(b).toLowerCase() === 'journal.json' ? 1 : 0;
      return am - bm || a.localeCompare(b);
    });
  }

  function asArray(value) { return Array.isArray(value) ? value : []; }
  function firstValue(...values) {
    return values.find(v => v !== undefined && v !== null && v !== '');
  }
  const CHECK_ALIASES = [
    ['External buy/sell side taken', ['externalbuysellside', 'externalliquidity', 'liquiditytaken', 'externalrange', 'buysellside', 'liquiditysweep']],
    ['DXY aligned', ['dxy', 'dxyaligned', 'dxyconfirmation', 'dxyalignment']],
    ['CISD candle closed', ['cisd', 'cisdclosed', 'cisdconfirmation', 'candleclosed']],
    ['Premium / discount', ['premiumdiscount', 'premiumordiscount', 'pdarray', 'discountpremium']],
    ['Target + reason', ['targetreason', 'targetandreason', 'targetdefined', 'target']],
    ['FVG', ['fvg', 'fairvaluegap']],
    ['SMT', ['smt', 'smtdivergence']],
    ['OTE', ['ote', 'optimaltradeentry']],
    ['50% retracement', ['50retracement', '50percentretracement', 'fiftypercent', 'midpoint']],
    ['Real displacement', ['realdisplacement', 'displacement', 'strongdisplacement']]
  ];
  function checkKey(value) { return String(value ?? '').toLowerCase().replace(/[^a-z0-9]/g, ''); }
  function canonicalCheck(value) {
    if (value && typeof value === 'object') value = firstValue(value.label, value.name, value.key, value.id, value.title, '');
    const k = checkKey(value);
    for (const [label, aliases] of CHECK_ALIASES) {
      const canonical = checkKey(label);
      if (k === canonical || aliases.some(a => k === a || k.includes(a) || a.includes(k) && k.length > 3)) return label;
    }
    return String(value ?? '').trim();
  }
  function normalizeLegacyChecks(t) {
    const raw = firstValue(t.checks, t.checklist, t.modelChecklist, t.aPlusChecklist, t.checklistItems, t.criteria, t.setupChecklist, null);
    const values = [];
    if (Array.isArray(raw)) {
      for (const item of raw) {
        if (item && typeof item === 'object') {
          const enabled = firstValue(item.checked, item.done, item.complete, item.completed, item.value, true);
          if (enabled === false || enabled === 0 || enabled === 'false') continue;
          const label = canonicalCheck(item);
          if (label) values.push(label);
        } else if (String(item ?? '').trim()) values.push(canonicalCheck(item));
      }
    } else if (raw && typeof raw === 'object') {
      for (const [key, value] of Object.entries(raw)) {
        const enabled = value && typeof value === 'object' ? firstValue(value.checked, value.done, value.complete, value.completed, value.value, false) : value;
        if (enabled === true || enabled === 1 || enabled === 'true' || enabled === 'checked') values.push(canonicalCheck(firstValue(value?.label, value?.name, key)));
      }
    }
    // Some older builds stored checklist flags directly on the trade object.
    const directKeys = {
      'External buy/sell side taken': ['externalBuySellSideTaken','externalLiquidity','liquidityTaken','externalRangeTaken','buySellSideTaken'],
      'DXY aligned': ['dxyAligned','dxyConfirmation','dxy'],
      'CISD candle closed': ['cisdCandleClosed','cisdClosed','cisd'],
      'Premium / discount': ['premiumDiscount','premiumOrDiscount'],
      'Target + reason': ['targetAndReason','targetReason','targetDefined'],
      'FVG': ['fvg','fairValueGap'],
      'SMT': ['smt','smtDivergence'],
      'OTE': ['ote','optimalTradeEntry'],
      '50% retracement': ['retracement50','fiftyPercentRetracement','halfRetracement'],
      'Real displacement': ['realDisplacement','displacement']
    };
    for (const [label, keys] of Object.entries(directKeys)) {
      if (keys.some(key => t[key] === true || t[key] === 1 || t[key] === 'true' || t[key] === 'checked')) values.push(label);
    }
    return [...new Set(values)];
  }
  function normalizeScreenshot(value) {
    if (value && typeof value === 'object') {
      if (Buffer.isBuffer(value)) return 'data:image/png;base64,' + value.toString('base64');
      if (Array.isArray(value.data) && (value.type === 'Buffer' || value.encoding === 'base64')) {
        const buffer = value.type === 'Buffer' ? Buffer.from(value.data) : Buffer.from(value.data.join(''), 'base64');
        return 'data:image/png;base64,' + buffer.toString('base64');
      }
      value = firstValue(value.dataUrl, value.dataURL, value.data, value.src, value.url, value.path, value.filePath, value.base64, '');
    }
    if (typeof value !== 'string' || !value.trim()) return '';
    const raw = value.trim();
    if (/^data:image\//i.test(raw)) return raw;
    if (/^https?:\/\//i.test(raw)) return raw;
    const candidates = [];
    let local = raw;
    if (/^file:/i.test(local)) {
      try { local = decodeURIComponent(local.replace(/^file:\/\//i, '').replace(/^\//, '')); } catch (_) {}
    }
    candidates.push(local, path.resolve(legacyBaseDir, local), path.resolve(userDataPath, local));
    for (const candidate of [...new Set(candidates)]) {
      try {
        if (!fs.existsSync(candidate) || !fs.statSync(candidate).isFile()) continue;
        const ext = path.extname(candidate).toLowerCase();
        const mime = ({'.jpg':'image/jpeg','.jpeg':'image/jpeg','.png':'image/png','.webp':'image/webp','.gif':'image/gif','.bmp':'image/bmp'}[ext]) || 'application/octet-stream';
        if (!mime.startsWith('image/')) continue;
        return 'data:' + mime + ';base64,' + fs.readFileSync(candidate).toString('base64');
      } catch (_) {}
    }
    // Preserve unprefixed base64 image data from legacy exports.
    if (raw.length > 256 && /^[A-Za-z0-9+/=\r\n]+$/.test(raw)) return 'data:image/png;base64,' + raw.replace(/\s/g, '');
    return raw;
  }
  function normalizeLegacyTrade(value) {
    const t = value && typeof value === 'object' ? value : {};
    const checks = normalizeLegacyChecks(t);
    return {
      ...t,
      direction: firstValue(t.direction, t.side, t.tradeDirection, '') ,
      setup: firstValue(t.setup, t.grade, t.setupGrade, t.setupGradeLabel, '') ,
      result: firstValue(t.result, t.outcome, t.tradeResult, '') ,
      r: firstValue(t.r, t.rr, t.rMultiple, t.rMultipleValue, '') ,
      pnl: firstValue(t.pnl, t.profitLoss, t.netPnl, t.profit, '') ,
      emotion: firstValue(t.emotion, t.mindset, t.tradeEmotion, '') ,
      entry: firstValue(t.entry, t.entryPrice, t.entryLevel, '') ,
      sl: firstValue(t.sl, t.stop, t.stopLoss, t.stopLossPrice, '') ,
      tp: firstValue(t.tp, t.target, t.takeProfit, t.targetPrice, '') ,
      note: firstValue(t.note, t.notes, t.tradeNote, t.journalNote, '') ,
      checks,
      shot1: normalizeScreenshot(firstValue(t.shot1, t.screenshot1, t.screenshot, t.contextScreenshot, t.screenshotContext, t.chartScreenshot, t.chartImage, t.image, '')) ,
      shot2: normalizeScreenshot(firstValue(t.shot2, t.screenshot2, t.executionScreenshot, t.screenshotExecution, t.executionImage, '')) ,
      tags: Array.isArray(t.tags) ? t.tags : (typeof t.tags === 'string' ? t.tags.split(',').map(x => x.trim()).filter(Boolean) : [])
    };
  }

  function normalizeLegacyDay(date, value) {
    if (!value || typeof value !== 'object' || Array.isArray(value)) return null;
    const day = {
      date: value.date || date,
      status: firstValue(value.status, value.dayStatus, 'Planned'),
      emotion: firstValue(value.emotion, value.dayEmotion, ''),
      note: firstValue(value.note, value.dayNotes, ''),
      tags: asArray(value.tags),
      sessions: { london: { trades: [] }, newyork: { trades: [] } }
    };
    for (const sessionName of ['london', 'newyork']) {
      const raw = (value.sessions && value.sessions[sessionName]) ||
        value[sessionName] || (sessionName === 'newyork' ? value.ny : null);
      if (!raw || typeof raw !== 'object') continue;
      // The previous desktop schema stored a single trade under session.trade
      // (for example day.london.trade), while the newer schema uses session.trades[].
      // Unwrap that legacy envelope before normalizing fields and embedded screenshot data URLs.
      if (Array.isArray(raw.trades)) {
        day.sessions[sessionName] = {
          ...raw,
          trades: raw.trades.map(item => normalizeLegacyTrade(item && item.trade && typeof item.trade === 'object' ? item.trade : item))
        };
        continue;
      }
      const legacyTrade = raw.trade && typeof raw.trade === 'object' ? raw.trade : raw;
      const t = normalizeLegacyTrade(legacyTrade);
      const hasTradeData = [
        t.direction, t.setup, t.result, t.r, t.pnl, t.entry, t.sl, t.tp,
        t.emotion, t.note, t.shot1, t.shot2
      ].some(v => v !== undefined && v !== null && v !== '') || t.checks.length || t.tags.length || raw.traded;
      if (hasTradeData) day.sessions[sessionName].trades = [t];
    }
    return day;
  }

  function hasMeaningfulTradeData(t) {
    if (!t || typeof t !== 'object') return false;
    const scalarKeys = ['direction','setup','result','r','pnl','emotion','entry','sl','tp','note','shot1','shot2'];
    if (scalarKeys.some(key => t[key] !== undefined && t[key] !== null && String(t[key]).trim() !== '')) return true;
    return asArray(t.checks).length > 0 || asArray(t.tags).length > 0;
  }

  function tradeIdentity(t) {
    const norm = v => String(v ?? '').trim().toLowerCase();
    const entry = norm(t.entry);
    const direction = norm(t.direction);
    if (entry && direction) return 'entry|' + direction + '|' + entry;
    const fields = ['direction', 'setup', 'result', 'r', 'pnl', 'entry', 'sl', 'tp'].map(k => norm(t[k]));
    const populated = fields.filter(Boolean).length;
    if (populated >= 3) return 'core|' + fields.join('|');
    // Only deduplicate weakly identified trades if their full user-entered content matches.
    return 'full|' + JSON.stringify({
      direction: t.direction || '', setup: t.setup || '', result: t.result || '',
      r: t.r || '', pnl: t.pnl || '', entry: t.entry || '', sl: t.sl || '',
      tp: t.tp || '', note: t.note || '', emotion: t.emotion || '',
      checks: asArray(t.checks), tags: asArray(t.tags), shot1: t.shot1 || '', shot2: t.shot2 || ''
    });
  }

  function mergeTrade(existing, legacy) {
    const out = { ...legacy, ...existing };
    let enriched = false;
    for (const key of ['direction','setup','result','r','pnl','emotion','entry','sl','tp','note','shot1','shot2']) {
      if ((out[key] === '' || out[key] === undefined || out[key] === null) &&
          legacy[key] !== '' && legacy[key] !== undefined && legacy[key] !== null) {
        out[key] = legacy[key]; enriched = true;
      }
    }
    for (const key of ['checks','tags']) {
      const merged = [...new Set([...asArray(existing[key]), ...asArray(legacy[key])])];
      if (merged.length !== asArray(existing[key]).length) enriched = true;
      out[key] = merged;
    }
    return { trade: out, enriched };
  }

  function mergeDay(existing, legacy, report) {
    if (!existing) {
      report.daysAdded++;
      report.tradesAdded += ['london','newyork'].reduce((n,s) => n + asArray(legacy.sessions?.[s]?.trades).length, 0);
      return legacy;
    }
    const out = { ...legacy, ...existing, date: existing.date || legacy.date };
    if ((!existing.status || existing.status === 'Planned') && legacy.status && legacy.status !== 'Planned') out.status = legacy.status;
    if (!existing.emotion && legacy.emotion) out.emotion = legacy.emotion;
    if (legacy.note && legacy.note !== existing.note) {
      if (!existing.note) out.note = legacy.note;
      else if (!String(existing.note).includes(String(legacy.note))) out.note = String(existing.note) + '\n\n[Recovered from previous journal]\n' + legacy.note;
    }
    out.tags = [...new Set([...asArray(existing.tags), ...asArray(legacy.tags)])];
    out.sessions = out.sessions || {};
    for (const s of ['london','newyork']) {
      const currentTrades = asArray(existing.sessions?.[s]?.trades).map(normalizeLegacyTrade);
      const oldTrades = asArray(legacy.sessions?.[s]?.trades).map(normalizeLegacyTrade);
      const merged = currentTrades.slice();
      for (const oldTrade of oldTrades) {
        const id = tradeIdentity(oldTrade);
        let index = merged.findIndex(t => tradeIdentity(t) === id);
        // Existing SQLite journals may contain a blank placeholder trade created
        // when the legacy nested .trade object was not understood by an earlier importer.
        // Fill that placeholder instead of adding a duplicate visible trade card.
        if (index < 0) index = merged.findIndex(t => !hasMeaningfulTradeData(t));
        if (index < 0) { merged.push(oldTrade); report.tradesAdded++; }
        else {
          const result = mergeTrade(merged[index], oldTrade);
          merged[index] = result.trade;
          if (result.enriched) report.tradesEnriched++;
        }
      }
      out.sessions[s] = { ...(existing.sessions?.[s] || legacy.sessions?.[s] || {}), trades: merged };
    }
    return out;
  }

  function mergeLegacyPayload(currentData, incomingData, report) {
    const sourceDays = incomingData && incomingData.days && typeof incomingData.days === 'object'
      ? incomingData.days
      : incomingData;
    if (!sourceDays || typeof sourceDays !== 'object' || Array.isArray(sourceDays)) return currentData;
    for (const [key, raw] of Object.entries(sourceDays)) {
      const date = raw && typeof raw.date === 'string' ? raw.date : key;
      if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) continue;
      const legacy = normalizeLegacyDay(date, raw);
      if (!legacy) continue;
      currentData.days[date] = mergeDay(currentData.days[date], legacy, report);
    }
    return currentData;
  }

  function importLegacy() {
    const sources = listLegacySources();
    const report = { filesFound: sources.length, filesRead: 0, daysAdded: 0, tradesAdded: 0, tradesEnriched: 0, sources: [] };
    if (!sources.length) { lastLegacyReport = report; return report; }
    const before = load();
    let merged = { version: 2, days: { ...before.days } };
    for (const file of sources) {
      try {
        const parsed = JSON.parse(fs.readFileSync(file, 'utf8'));
        legacyBaseDir = path.dirname(file);
        const beforeCounts = { daysAdded: report.daysAdded, tradesAdded: report.tradesAdded, tradesEnriched: report.tradesEnriched };
        merged = mergeLegacyPayload(merged, parsed, report);
        report.filesRead++;
        report.sources.push({ file, daysAdded: report.daysAdded - beforeCounts.daysAdded, tradesAdded: report.tradesAdded - beforeCounts.tradesAdded });
      } catch (error) {
        report.sources.push({ file, error: 'Could not read valid journal JSON' });
      }
    }
    if (report.daysAdded || report.tradesAdded || report.tradesEnriched) {
      makeBackup(); // recovery point before merging anything into the current SQLite journal
      save(merged);
    }
    lastLegacyReport = report;
    return report;
  }

  function importFile(filePath) {
    if (typeof filePath !== 'string' || !fs.existsSync(filePath)) throw new Error('Selected JSON file could not be found.');
    const parsed = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    legacyBaseDir = path.dirname(filePath);
    const before = load();
    const report = { filesFound: 1, filesRead: 1, daysAdded: 0, tradesAdded: 0, tradesEnriched: 0, sources: [{ file: filePath }] };
    const merged = mergeLegacyPayload({ version: 2, days: { ...before.days } }, parsed, report);
    if (report.daysAdded || report.tradesAdded || report.tradesEnriched) {
      makeBackup();
      save(merged);
    }
    lastLegacyReport = report;
    return report;
  }

  function getLegacyReport() { return lastLegacyReport; }

  function status() {
    const count = db.prepare('SELECT COUNT(*) AS n FROM days').get().n;
    return { dbPath, backupDir, dayCount: count, version: 2 };
  }

  return { load, save, restore, deleteDay, exportJson, makeBackup, status, importLegacy, importFile, getLegacyReport, close: () => db.close() };
}

module.exports = { createStorage };

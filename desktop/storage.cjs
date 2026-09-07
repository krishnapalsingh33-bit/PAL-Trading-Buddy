const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const STORAGE_VERSION = 2;
const MAX_BACKUPS = 20;
const MAX_SCREENSHOT_BYTES = 10 * 1024 * 1024;

function createStorage(userDataPath) {
  const root = path.join(userDataPath, 'Trading Discipline Tracker');
  const backupDir = path.join(root, 'backups');
  const screenshotsDir = path.join(root, 'screenshots');
  const journalPath = path.join(root, 'journal.json');
  const settingsPath = path.join(root, 'settings.json');

  fs.mkdirSync(backupDir, { recursive: true });
  fs.mkdirSync(screenshotsDir, { recursive: true });

  function emptyJournal() {
    return {
      version: STORAGE_VERSION,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      days: {}
    };
  }

  function normalize(data) {
    if (!data || typeof data !== 'object' || Array.isArray(data)) return emptyJournal();
    const sourceDays = data.days && typeof data.days === 'object' && !Array.isArray(data.days)
      ? data.days
      : data;

    const normalized = {
      version: STORAGE_VERSION,
      createdAt: typeof data.createdAt === 'string' ? data.createdAt : new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      days: {}
    };

    for (const [date, value] of Object.entries(sourceDays || {})) {
      if (!value || typeof value !== 'object' || Array.isArray(value)) continue;
      normalized.days[date] = value;
    }

    return normalized;
  }

  function readJson(filePath, fallback) {
    try {
      if (!fs.existsSync(filePath)) return fallback;
      const raw = fs.readFileSync(filePath, 'utf8');
      return JSON.parse(raw);
    } catch (_) {
      return fallback;
    }
  }

  function writeJsonAtomic(filePath, data) {
    const tempPath = `${filePath}.tmp-${process.pid}-${Date.now()}`;
    const payload = JSON.stringify(data, null, 2);
    fs.writeFileSync(tempPath, payload, { encoding: 'utf8', flag: 'w' });
    try {
      fs.renameSync(tempPath, filePath);
    } catch (error) {
      try { fs.rmSync(filePath, { force: true }); } catch (_) {}
      fs.renameSync(tempPath, filePath);
    }
  }

  function listBackups() {
    try {
      return fs.readdirSync(backupDir)
        .filter(file => /^journal-.*\.json$/i.test(file))
        .sort()
        .reverse();
    } catch (_) {
      return [];
    }
  }

  function pruneBackups() {
    const files = listBackups();
    for (const file of files.slice(MAX_BACKUPS)) {
      try { fs.rmSync(path.join(backupDir, file), { force: true }); } catch (_) {}
    }
  }

  function makeBackup() {
    if (!fs.existsSync(journalPath)) return null;
    const stamp = new Date().toISOString().replace(/[:.]/g, '-');
    const target = path.join(backupDir, `journal-${stamp}.json`);
    try {
      fs.copyFileSync(journalPath, target, fs.constants.COPYFILE_EXCL);
    } catch (_) {
      try { fs.copyFileSync(journalPath, target); } catch (_) { return null; }
    }
    pruneBackups();
    return target;
  }

  function load() {
    const data = readJson(journalPath, emptyJournal());
    return normalize(data);
  }

  function save(data) {
    const current = load();
    const normalized = normalize(data);
    normalized.createdAt = current.createdAt || normalized.createdAt;

    if (fs.existsSync(journalPath)) makeBackup();
    writeJsonAtomic(journalPath, normalized);
    return load();
  }

  function restore(payload) {
    const current = load();
    const normalized = normalize(payload);
    normalized.createdAt = current.createdAt || normalized.createdAt;

    if (fs.existsSync(journalPath)) makeBackup();
    writeJsonAtomic(journalPath, normalized);
    return load();
  }

  function exportJson() {
    return JSON.stringify(load(), null, 2);
  }

  function getSettings() {
    return readJson(settingsPath, {});
  }

  function saveSettings(settings) {
    const safe = settings && typeof settings === 'object' && !Array.isArray(settings) ? settings : {};
    writeJsonAtomic(settingsPath, safe);
    return getSettings();
  }

  function safeScreenshotPath(filename) {
    if (typeof filename !== 'string' || !filename) throw new Error('Invalid screenshot filename');
    const safe = path.basename(filename);
    if (safe !== filename || safe.includes('..')) throw new Error('Invalid screenshot filename');
    const full = path.join(screenshotsDir, safe);
    if (!full.startsWith(screenshotsDir + path.sep)) throw new Error('Invalid screenshot path');
    return full;
  }

  function saveScreenshot(payload) {
    if (!payload || typeof payload !== 'object') throw new Error('Invalid screenshot payload');
    const dataUrl = String(payload.dataUrl || '');
    const match = dataUrl.match(/^data:(image\/(?:png|jpeg|webp));base64,(.+)$/i);
    if (!match) throw new Error('Unsupported screenshot format');
    const data = Buffer.from(match[2], 'base64');
    if (!data.length || data.length > MAX_SCREENSHOT_BYTES) throw new Error('Screenshot is too large');
    const ext = match[1].toLowerCase() === 'image/png' ? 'png' : match[1].toLowerCase() === 'image/webp' ? 'webp' : 'jpg';
    const filename = `${Date.now()}-${crypto.randomUUID()}.${ext}`;
    const filePath = safeScreenshotPath(filename);
    fs.writeFileSync(filePath, data, { flag: 'w' });
    return { filename, size: data.length, type: match[1].toLowerCase() };
  }

  function readScreenshot(filename) {
    try {
      const filePath = safeScreenshotPath(filename);
      if (!fs.existsSync(filePath)) return null;
      const ext = path.extname(filePath).toLowerCase();
      const mime = ext === '.png' ? 'image/png' : ext === '.webp' ? 'image/webp' : 'image/jpeg';
      return `data:${mime};base64,${fs.readFileSync(filePath).toString('base64')}`;
    } catch (_) {
      return null;
    }
  }

  function deleteScreenshot(filename) {
    try {
      fs.rmSync(safeScreenshotPath(filename), { force: true });
      return true;
    } catch (_) {
      return false;
    }
  }

  function status() {
    const journal = load();
    return {
      storageRoot: root,
      journalPath,
      backupDir,
      screenshotsDir,
      settingsPath,
      dayCount: Object.keys(journal.days).length,
      backupCount: listBackups().length,
      version: STORAGE_VERSION
    };
  }

  return {
    load,
    save,
    restore,
    exportJson,
    makeBackup,
    getSettings,
    saveSettings,
    saveScreenshot,
    readScreenshot,
    deleteScreenshot,
    status,
    close: () => {}
  };
}

module.exports = { createStorage };

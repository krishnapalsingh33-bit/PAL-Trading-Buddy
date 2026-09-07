const fs = require('fs');
const path = require('path');

const STORAGE_VERSION = 2;
const MAX_BACKUPS = 20;

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
    status,
    close: () => {}
  };
}

module.exports = { createStorage };

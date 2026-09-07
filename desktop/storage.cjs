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

  function status() {
    const count = db.prepare('SELECT COUNT(*) AS n FROM days').get().n;
    return { dbPath, backupDir, dayCount: count, version: 2 };
  }

  return { load, save, restore, exportJson, makeBackup, status, close: () => db.close() };
}

module.exports = { createStorage };

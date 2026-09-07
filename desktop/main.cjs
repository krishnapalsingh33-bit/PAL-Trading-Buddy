const { app, BrowserWindow, Menu, shell, ipcMain, dialog } = require('electron');
const path = require('path');
const fs = require('fs');
const { createStorage } = require('./storage.cjs');

let storage = null;

function createWindow() {
  const win = new BrowserWindow({
    width: 1420,
    height: 920,
    minWidth: 1100,
    minHeight: 720,
    backgroundColor: '#151515',
    title: 'Trading Discipline Tracker',
    webPreferences: {
      contextIsolation: true,
      nodeIntegration: false,
      sandbox: false,
      preload: path.join(__dirname, 'preload.cjs')
    }
  });

  Menu.setApplicationMenu(null);
  win.loadFile(path.join(__dirname, 'trading-discipline-tracker-final.html'));

  win.webContents.on('did-finish-load', () => {
    const patch = `(() => {
      const bindDayFields = () => {
        ['dayStatus', 'dayEmotion', 'dayNote'].forEach((id) => {
          const field = document.getElementById(id);
          if (!field || field.dataset.tdtDayBound === '1') return;
          const markDirty = () => {
            const saveButton = document.getElementById('saveDay');
            if (saveButton) saveButton.style.display = 'inline-block';
          };
          field.addEventListener('input', markDirty);
          field.addEventListener('change', markDirty);
          field.dataset.tdtDayBound = '1';
        });
      };
      bindDayFields();
      new MutationObserver(bindDayFields).observe(document.body, { childList: true, subtree: true });
    })();`;
    win.webContents.executeJavaScript(patch, true).catch(() => {});
  });

  win.webContents.setWindowOpenHandler(({ url }) => {
    if (/^https?:\/\//i.test(url)) shell.openExternal(url);
    return { action: 'deny' };
  });
}

function registerIpc() {
  ipcMain.handle('db:load', () => storage.load());
  ipcMain.handle('db:save', (_, data) => storage.save(data));
  ipcMain.handle('db:backup', () => storage.makeBackup());
  ipcMain.handle('db:restore', (_, payload) => storage.restore(payload));
  ipcMain.handle('db:status', () => storage.status());
  ipcMain.handle('db:save-screenshot', (_, payload) => storage.saveScreenshot(payload));
  ipcMain.handle('db:read-screenshot', (_, filename) => storage.readScreenshot(filename));
  ipcMain.handle('db:delete-screenshot', (_, filename) => storage.deleteScreenshot(filename));
  ipcMain.handle('db:export-json', async () => {
    const result = await dialog.showSaveDialog({
      title: 'Export Trading Journal',
      defaultPath: path.join(app.getPath('documents'), 'TradingDisciplineTracker-backup.json'),
      filters: [{ name: 'JSON', extensions: ['json'] }]
    });
    if (result.canceled || !result.filePath) return { canceled: true };
    fs.writeFileSync(result.filePath, storage.exportJson(), 'utf8');
    return { canceled: false, filePath: result.filePath };
  });
}

app.whenReady().then(() => {
  storage = createStorage(app.getPath('userData'));
  registerIpc();
  createWindow();
  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('before-quit', () => {
  try { storage?.makeBackup(); } catch (_) {}
  try { storage?.close(); } catch (_) {}
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});

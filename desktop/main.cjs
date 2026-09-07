const { app, BrowserWindow, Menu, shell, ipcMain, dialog } = require('electron');
const path = require('path');
const fs = require('fs');
const { createStorage } = require('./storage.cjs');

let storage = null;

function createWindow() {
  const win = new BrowserWindow({
    width: 1420,
    height: 900,
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
  win.loadFile(path.join(__dirname, 'trading-discipline-tracker-v2.html'));

  win.webContents.on('did-finish-load', () => {
    const premiumScript = path.join(__dirname, 'v2.1-premium.js');
    if (!fs.existsSync(premiumScript)) return;
    const script = fs.readFileSync(premiumScript, 'utf8');
    win.webContents.executeJavaScript(script, true).catch(() => {});
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

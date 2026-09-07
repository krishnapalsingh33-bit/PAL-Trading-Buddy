const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('tdt', {
  db: {
    load: () => ipcRenderer.invoke('db:load'),
    save: (data) => ipcRenderer.invoke('db:save', data),
    backup: () => ipcRenderer.invoke('db:backup'),
    restore: (payload) => ipcRenderer.invoke('db:restore', payload),
    exportJson: () => ipcRenderer.invoke('db:export-json'),
    status: () => ipcRenderer.invoke('db:status'),
    saveScreenshot: (payload) => ipcRenderer.invoke('db:save-screenshot', payload),
    readScreenshot: (filename) => ipcRenderer.invoke('db:read-screenshot', filename),
    deleteScreenshot: (filename) => ipcRenderer.invoke('db:delete-screenshot', filename)
  }
});

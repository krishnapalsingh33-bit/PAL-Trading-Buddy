const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('tdt', {
  db: {
    load: () => ipcRenderer.invoke('db:load'),
    save: (data) => ipcRenderer.invoke('db:save', data),
    backup: () => ipcRenderer.invoke('db:backup'),
    restore: (payload) => ipcRenderer.invoke('db:restore', payload),
    exportJson: () => ipcRenderer.invoke('db:export-json'),
    status: () => ipcRenderer.invoke('db:status')
  }
});


//Loading the required modules
const path = require('path');
const url = require('url');
const electron = require('electron');

const {app, BrowserWindow} = electron;  //Loading specfic modules from Electron


let main_window  // Keep a global reference of the window object


// Functions
// =================================================================================================

function start_main_window ()
{
  // Create the browser window.
  main_window = new BrowserWindow({width: 800, height: 500})

  //Load the index.html of the app.
  main_window.loadURL(url.format({
    pathname: path.join(__dirname, 'main.html'),
    protocol: 'file:',
    slashes: true
  }))

  // Emitted when the window is closed.
  main_window.on('closed', function () {
    // Dereference the window object, usually you would store windows
    // in an array if your app supports multi windows.
    main_window = null
  })
}


// Main
// =================================================================================================

app.on('ready', start_main_window)

// Quit when all windows are closed.
app.on('window-all-closed', function () {
  // On OS X it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', function () {
  // On OS X it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (mainWindow === null) {
    start_main_window()
  }
})
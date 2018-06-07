
//Loading the required modules
const electron = require('electron');
const path = require('path');
const url = require('url');
const exec = require('child_process').exec;

const {app, BrowserWindow, Menu} = electron;  //Loading specfic modules from Electron


// Globals
// =================================================================================================

let main_window  // Keep a global reference of the window object

const main_menu_template = 
[
  {
    label: 'File',
    submenu:
    [
      {label: 'Quit'}
    ]
  }
];


// Functions
// =================================================================================================

function start_main_window ()
{

    // Create the browser window.
    main_window = new BrowserWindow({width: 900, height: 600})

    //Load the index.html of the app.
    main_window.loadURL(url.format({
        pathname: path.join(__dirname, 'login.html'),
        protocol: 'file:',
        slashes: true
    }))

    // Emitted when the window is closed.
    main_window.on('closed', function () {
        // Dereference the window object, usually you would store windows
        // in an array if your app supports multi windows.
        main_window = null
    })

    const main_menu = Menu.buildFromTemplate(main_menu_template);

    Menu.setApplicationMenu(main_menu);

}


// Main
// =================================================================================================

// If MAC, add empty object to menu
if (process.platform == 'darwin')
{
  main_menu_template.unshift({});
}

if (process.env.NODE_ENV !== 'production')
{
    main_menu_template.push(
    {
        label: 'Developer Tools',
        submenu: 
        [
            {
                label: 'Toggle Developer Tools',
                click(item,focusedWindow) 
                {
                    focusedWindow.toggleDevTools();
                }
            },
            {
                role: 'reload'
            }
        ]
    });
}

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

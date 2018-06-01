// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// All of the Node.js APIs are available in this process.

const { remote } = require('electron')
const url = require('url')
const path = require('path')

function openMain() {
   remote.getCurrentWindow().loadURL(url.format({
    pathname: path.join(__dirname, 'spyn_main.html'),
    protocol: 'file:',
    slashes: true
  }))
}

document.querySelector('#submit').addEventListener('click', openMain)

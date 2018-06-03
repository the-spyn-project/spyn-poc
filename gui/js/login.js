// Loading modules

const { remote } = require('electron')
const url = require('url')
const path = require('path')

const Menu = remote;

// Functions
// =================================================================================================

function openMain() 
{

	remote.getCurrentWindow().loadURL(url.format({
		pathname: path.join(__dirname, '/../index.html'),
		protocol: 'file:',
		slashes: true
  	}))

	const main_menu = Menu.buildFromTemplate(main_menu_template);

	Menu.setApplicationMenu(main_menu)
}

const main_menu_template = 
[
	{
		label: 'File',
		submenu:
		[
			{label: 'Developer Mode'},
			{label: 'Quit'}
		]
	},
	{
		label: 'View',
		submenu:
		[
			{label: 'Full Screen'},
			{label: 'Docked'}
		],
	}
];


// Listeners
// =================================================================================================

document.querySelector('#submit').addEventListener('click', openMain)

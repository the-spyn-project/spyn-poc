var exec = require('child_process').exec;
var execSync = require('child_process').execSync;

/**
Given:
    command: command to be executed
    callback: callback function with error, stdout, stderr as arguments

This method executes command and runs callback with
error, stdout, stderr. callback is a user definable function
taking error, stdout, stderr from executing the command.

**/
// https://stackoverflow.com/questions/12941083/get-the-output-of-a-shell-command-in-node-js
exports.execute = function (command, callback) {
    exec(command, {windowsHide:true}, function(error, stdout, stderr){ callback(error, stdout, stderr); });
};

/**
Given: 
     cmd - command to be executed

This method executes command cmd and logs
the results on console.
**/
exports.runCommand = function (cmd) {
    exec(cmd, {windowsHide:true}, function (error, stdout, stderr) {
    console.log('stdout: ' + stdout);
    console.log('stderr: ' + stderr);
    if (error !== null) {
      console.log('docker error: ' + error);
    }
    });
}; 

/**
Given: 
     cmd - command to be executed

Returns:
     res - stdout from command execution
This method executes command cmd and returns stdout. 
All other codes are blocked from execution until child
process for the command exits.
**/
exports.runCommandSyn = function (cmd) {
    res = execSync(cmd, {windowsHide:true});
    return res;
}


// Importing modules
// =================================================================================================

const net = require('net');
const Web3 = require('web3');
window.$ = window.jQuery = require('jquery');


// Setting Provider
// =================================================================================================

var web3 = new Web3(new Web3.providers.IpcProvider(
					  '/home/veda-sadhak/Desktop/Ethereum/Blockchain/geth.ipc', net)); 
var exec = require('child_process').exec;
var cmd = require('./dockerCmd');

// Main
// =================================================================================================

$(document).ready(function(){
    
    $("#view_network_page").hide();
	$("#submit_job_page").hide();
    $("#view_acc_page").hide();
    $("#login_page").hide();
    $("#logout_page").hide();
	$("#supply_resources_page").hide();
	$("#view_network_page").show();	

    $("#view_network_btn").click(function(){
    	$("#supply_resources_page").hide();	
    	$("#submit_job_page").hide();
        $("#view_acc_page").hide();
        $("#login_page").hide();
        $("#logout_page").hide();
    	$("#view_network_page").show();
        cmd.execute('docker container exec ff0efc08bf8e ls', function (error, stdout, stderr) {document.write(stdout);});
    });

    $("#supply_resources_btn").click(function(){
    	$("#view_network_page").hide();
    	$("#submit_job_page").hide();
        $("#view_acc_page").hide();
        $("#login_page").hide();
        $("#logout_page").hide();
    	$("#supply_resources_page").show();	
    });

    $("#submit_job_btn").click(function(){
    	$("#view_network_page").hide();
    	$("#supply_resources_page").hide();	
        $("#view_acc_page").hide();
        $("#login_page").hide();
        $("#logout_page").hide();
        $("#submit_job_page").show();
    });

    $("#view_acc_btn").click(function(){
    	$("#view_network_page").hide();
    	$("#supply_resources_page").hide();	
    	$("#submit_job_page").hide();
        $("#login_page").hide();
        $("#logout_page").hide();
    	$("#view_acc_page").show();
    });

    $("#login_btn").click(function(){
    	$("#view_network_page").hide();
    	$("#supply_resources_page").hide();	
    	$("#submit_job_page").hide();
        $("#view_acc_page").hide();
        $("#logout_page").hide();
    	$("#login_page").show();

    	web3.eth.getAccounts(function(err, accounts) 
		{ 
			for (var i = 0; i < accounts.length; i++)
			{
				$("#login_page").append("<div class='accounts_list_item'>"+
											"<div class='accounts_list_text'>"+
										 		accounts[i]+
										 	"</div>"+
										"</div>");
			}
		});
    });

    $("#logout_btn").click(function(){
    	$("#view_network_page").hide();
    	$("#supply_resources_page").hide();	
    	$("#submit_job_page").hide();
        $("#view_acc_page").hide();
        $("#login_page").hide();
    	$("#logout_page").show();
    });

});

function displayInfo(){
  
  exec('docker container exec ff0efc08bf8e ls', {windowsHide:true}, function (error, stdout, stderr) {
  console.log('stdout: ' + stdout);
  console.log('stderr: ' + stderr);
  document.write(stdout);
  if (error !== null) {
    console.log('docker error: ' + error);
  }
  });
  
}

function createNvidiaContainer(container_addr){
    exec('nvidia-docker create -ti ' + container_addr + ' /bin/bash', {windowsHide:true}, function (error, stdout, stderr) {
    console.log('stdout: ' + stdout);
    console.log('stderr: ' + stderr);
    if (error !== null) {
      console.log('docker error: ' + error);
    }
    });
}

function removeContainer(container_id){
    exec('nvidia-docker rm -f ' + container_id, {windowsHide:true}, function (error, stdout, stderr) {
    console.log('stdout: ' + stdout);
    console.log('stderr: ' + stderr);
    if (error !== null) {
      console.log('docker error: ' + error);
    }
    });
}

function startContainer(container_id){
    exec('nvidia-docker start ' + container_id, {windowsHide:true}, function (error, stdout, stderr) {
    console.log('stdout: ' + stdout);
    console.log('stderr: ' + stderr);
    if (error !== null) {
      console.log('docker error: ' + error);
    }
    });

}


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
var docker = require('./dockerCmdLib');

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

        // synchronous
        document.write(docker.cp('', 'login.js fa903b5ba185:login.js'));
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



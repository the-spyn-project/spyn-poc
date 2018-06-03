window.$ = window.jQuery = require('jquery');

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
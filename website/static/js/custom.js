$(document).ready(function(){

	// adding twitter bootstrap "$" before cost field in "post task form"
	$("#post_task_cost").parent().addClass("input-group");
	$("#post_task_cost").before("<span class=\"input-group-addon\">$</span>");

	$("#register_form").submit(function(event){
		console.log("registration");

		event.preventDefault();

		$.ajax({
                url: $(this).attr('action'),
                type: $(this).attr('method'),
                data: $(this).serialize(),
                cache: false,
                success: function(response){
                    if (response == 'OK'){
                        //successful register redirect
                        $("#reg_alert_success").show();
                        $("#register_form")[0].reset();
                    } else if (response == 'EXISTS') {
                        $("#reg_alert_exists").show();
                    } else if (response == 'NOTVALID'){
                    	$("#reg_alert_not_valid").show();
                    } else {
                    	console.log("smth strange");
                    }
                }
        });
	});

	$("#login_form").submit(function(event){
		console.log("autorization & logging in");

		event.preventDefault();

		$.ajax({
                url: $(this).attr('action'),
                type: $(this).attr('method'),
                data: $(this).serialize(),
                cache: false,
                success: function(response){
                    if (response == 'OK'){
                        //successful register redirect
                        document.location.href = '/profile/';
                    } else if (response == 'CANT') {
                        $("#login_alert_doesnt_exist").show();
                    } else if (response == 'NOTVALID'){
                    	$("#login_alert_not_valid").show();
                    } else {
                    	console.log("smth strange");
                    }
                }
        });
	});

	// adding boostrap help-block class for tips
	$(".helptext").addClass("help-block");
	$("#post_form").submit(function(event){
		console.log("posting the task");

		event.preventDefault();

		$.ajax({
                url: $(this).attr('action'),
                type: $(this).attr('method'),
                data: $(this).serialize(),
                cache: false,
                success: function(response){
                    if (response == 'OK'){
                        //successful register redirect
                        $("#post_alert_success").show();
                        $("#post_form")[0].reset();
                    } else if (response == 'NOTVALID'){
                    	$("#post_task_alert_not_valid").show();
                    } else {
                    	console.log("smth strange");
                    }
                }
        });
	});


	$("form[id*=take_task_form").submit(function(event){
		console.log("posting the task");

		event.preventDefault();
		var currentForm = $(this);

		$.ajax({
                url: $(this).attr('action'),
                type: $(this).attr('method'),
                data: $(this).serialize(),
                cache: false,
                success: function(response){
                    if (response == 'OK'){
                        //successful take_task
                        $("#take_task_alert_success").show();
                        currentForm.hide();
                    } else if (response == 'NOSUCHTASK') {
                        $("#take_task_alert_no_such").show();
                    } else if (response == 'OCCUPIED'){
                    	$("#take_task_alert_no_occupied").show();
                    } else {
                    	console.log("smth strange");
                    }
                }
        });
	});
});
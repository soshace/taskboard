$(document).ready(function(){
	$("#register_form").submit(function(event){
		console.log("registration");
		console.log($(this).attr('method'));

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
                        $(this)[0].reset();
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
});
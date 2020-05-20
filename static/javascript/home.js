document.addEventListener("DOMContentLoaded", function(){

    let user_email = $('#email');
    let user_pwd = $('#pwd');


    function invalid_input(element){
		element.css("box-shadow", "0 0 10px rgb(255, 0, 0)");
	}

	function valid_input(element) {
		element.css("box-shadow", "0 0 10px rgb(0, 255, 63)");
	}

	function password_strength(element) {

	}

   // When the user ID form is submitted, POST input to /process and if the user ID exists, redirect to welcome page
	// $('#form').on('submit', function(event) {
	// 	$.ajax({
	// 		data: {
	// 		userEmail: user_email.val(),
   //              userPassword: user_pwd.val()
   //
	// 		},
	// 		type: 'POST',
	// 		url: '/submitform',
	// 		success: function (response) {
	// 			console.log(response);
   //
	// 		}
	// 	});
	// 	// HTML automatically tries to post the form, we therefore manually stop this
	// 	event.preventDefault();
	// });
});
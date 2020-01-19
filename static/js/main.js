
$(document).ready(function() {
	console.log("clicked0");

	$('#next_img_btn').click(function(){
		$("#next_img_btn").html('Next');
		console.log("clicked1");

		$.ajax({
			url: "/",
			type: "GET",
			success: function(response) {
				$('#ad-img').attr('src', '/static/images/drac.jpg');
				// $("#ad-img").attr('src', '/static/' + response);
				console.log("clicked2");
			},
			error: function(xhr) {
			//Do Something to handle error
			}
		});
	});
	
});


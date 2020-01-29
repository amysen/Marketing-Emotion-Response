
$(document).ready(function() {
	var clicks = 0;
	$('#next_img_btn').click(function(){
		clicks += 1;
		$("#next_img_btn").html('Next');
		
		$.ajax({
			url: "/",
			type: "GET",
			success: function(response) {
				switch (clicks) {
				case 1:
					$('#ad').attr('src', 'static/images/drac.jpg');
					break;
				case 2:
					$('#ad').attr('src', 'static/images/McD.jpg');
					break;
				default:
					$('#ad').attr('src', 'static/images/pollution.jpg');

			}

			setTimeout(function (){

			  // Actions to be delayed.
			  $.getJSON('/advert',
					function(data) {
						//do nothing
						console.log("advert response detection");
				});

			}, 500);

			

			},
			error: function(xhr) {
			//Do Something to handle error
			}
		});

	});
	
});


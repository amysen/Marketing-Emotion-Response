
$(document).ready(function() {
	$('#next_img_btn').submit(function(){
		var ad_btn = document.getElementById("next_img_btn")
		ad_btn.value = "Next";
		console.log("clicked1");

		$.ajax({
			url: "{{ url_for ('ad_01') }}",
			type: "GET",
			success: function(response) {
				$("#ad-img").attr('src', '/static/' + response);
				console.log("clicked2");
				// $("next_img_btn").value('Next >');
			},
			error: function(xhr) {
			//Do Something to handle error
			}
		});
	});
});
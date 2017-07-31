$(document).ready(function() {
	google.maps.event.addDomListener(window, 'load', initialize);
});

function initialize() {
	var myCenter = new google.maps.LatLng(24.7867784, 120.9952533);
	var mapProp = {
		center: myCenter,
		zoom: 15,
		scrollwheel: true,
		draggable: true,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
	var marker = new google.maps.Marker({
	  position: myCenter,
	});
	marker.setMap(map);
}


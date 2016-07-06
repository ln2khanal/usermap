 function locus() {
     var lat = $("#from_filter option:selected").val();
     var lng = $("#to_filter option:selected").val();
     if (lat == null || lng == null) {
         console.log('Source or Destination missing!');
         alert('Source or Destination missing!');
         return;
     }
     $.get( "/route/getallroutes/",'from_filter='+ $('#from_filter').val() + '&to_filter=' + $('#to_filter').val(), function(data){
         prepareAndRenderRoutes(data);
     })
 }

 function prepareAndRenderRoutes(data) {
    var mapOptions = {
        center: new google.maps.LatLng(27.674201, 85.316721),
        zoom: 8,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    var map = new google.maps.Map(document.getElementById("map"), mapOptions);

    var directionsService = new google.maps.DirectionsService();

     for (var user in data){
        var request = {
            'origin': new google.maps.LatLng(data[user].source.lat, data[user].source.lng),
            'destination': new google.maps.LatLng(data[user].destination.lat, data[user].destination.lng),
            'travelMode': google.maps.DirectionsTravelMode.DRIVING
        };

        directionsService.route(request, function(response, status) {
            if(status == google.maps.DirectionsStatus.OK) {
                renderRoute(map, response);
            }
        });
    }
 }

 function renderRoute(map, response) {
    var directionsDisplay = new google.maps.DirectionsRenderer({ suppressMarkers: false, suppressInfoWindows: true });
    directionsDisplay.setMap(map);
    directionsDisplay.setDirections(response);
 }

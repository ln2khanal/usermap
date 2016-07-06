function renderRoute(map, response) {
        var directionsDisplay = new google.maps.DirectionsRenderer({ suppressMarkers: false, suppressInfoWindows: true });
        directionsDisplay.setMap(map);
        directionsDisplay.setDirections(response);
     }

    function loadNow(data) {
        var directionsService = new google.maps.DirectionsService();
        var mapOptions = {
            center: new google.maps.LatLng(27.674201, 85.316721),
            zoom: 4,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        var map = new google.maps.Map(document.getElementById("singleRoute"), mapOptions);

        var request = {
            'origin': new google.maps.LatLng(data.source.lat, data.source.lng),
            'destination': new google.maps.LatLng(data.destination.lat, data.destination.lng),
            'travelMode': google.maps.DirectionsTravelMode.DRIVING
        };

        directionsService.route(request, function(response, status) {
            if(status == google.maps.DirectionsStatus.OK) {
                renderRoute(map, response);
            } else {
                window.alert('Directions request failed due to ' + status);
            }
        });
    }

    $(function() {
        $('[data-popup-open]').on('click', function(e)  {
            var targeted_popup_class = jQuery(this).attr('data-popup-open');
            $('[data-popup="' + targeted_popup_class + '"]').fadeIn(350);
            e.preventDefault();
            $.get( "/route/userroute/",'user='+ $(this).attr("user"), function(data){
                loadNow(data);
            });
        });

        $('[data-popup-close]').on('click', function(e)  {
            var targeted_popup_class = jQuery(this).attr('data-popup-close');
            $('[data-popup="' + targeted_popup_class + '"]').fadeOut(350);
            e.preventDefault();
        });
    });
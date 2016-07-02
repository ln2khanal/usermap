
  function initMap() {
    var myLatLng = {lat: 27.6834812, lng: 85.3268499};

    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 8,
      center: myLatLng
    });

    var marker = new google.maps.Marker({
      position: myLatLng,
      map: map,
      title: 'Hello World!'
    });
  }

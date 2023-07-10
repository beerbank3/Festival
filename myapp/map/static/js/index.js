document.addEventListener("DOMContentLoaded", function() {
  const markers = document.querySelectorAll(".leaflet-interactive");

  markers.forEach(function(marker) {
      marker.addEventListener("click", function() {
          var cityName = this.getAttribute("data-name");
          console.log(cityName);
      });
  });
});

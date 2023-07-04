document.addEventListener("DOMContentLoaded", function() {
  const markers = document.querySelector("leaflet-interactive");

  Array.from(markers).forEach(function(marker) {
      marker.addEventListener("click", function() {
          var cityName = this.getAttribute("data-name");
          console.log(cityName);
          console.log("check")
      });
  });
});

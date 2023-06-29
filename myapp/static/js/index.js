console.log("cascsa");
var mapElement = document.getElementById('map');
var map = L.map(mapElement);

// 지도에 타일 레이어 추가 (예시: OpenStreetMap 타일 사용)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

// 마커 클릭 이벤트 리스너 추가
var marker = L.marker([marker_latitude, marker_longitude]).addTo(map);
marker.on('click', function(e) {
  // 마커를 클릭했을 때 수행할 동작을 여기에 작성합니다.
  console.log("cascsa");
  // 클릭 이벤트 발생 시 동작할 코드를 작성하세요.
});
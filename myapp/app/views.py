from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy, reverse
import folium

class Index(View):

    def get(self, request):

        latitude = 37.5665
        longitude = 126.9780
        # folium을 사용하여 지도 생성
        m = folium.Map(location=[latitude, longitude], zoom_start=12)

        # folium에 마커 추가
        cities = [
            {'name': '서울', 'location': [37.5665, 126.9780]},
            {'name': '부산', 'location': [35.1796, 129.0750]},
            {'name': '인천', 'location': [37.4563, 126.7052]},
            {'name': '대구', 'location': [35.8714, 128.6014]},
            {'name': '광주', 'location': [35.1595, 126.8526]},
            {'name': '대전', 'location': [36.3504, 127.3845]},
        ]

        # 마커 클릭 시 호출되는 JavaScript 함수
        click_script = """
        function onMarkerClick(e) {
            var cityName = e.target.options.cityName;
            alert("마커를 클릭했습니다.\n선택된 도시: " + cityName);
        }
        """
        # 대도시 마커 추가
        for city in cities:
            marker = folium.Marker(
                location=city['location'],
                popup=city['name'],
                icon=folium.Icon(icon='cloud')
            ).add_to(m)

        marker.add_child(folium.Popup(city['name']))  # 팝업을 마커의 자식으로 추가
        m.add_child(marker)  # 마커를 맵에 추가

        # folium 지도를 HTML로 변환하여 템플릿에 전달
        map_html = m.get_root().render()

        # HTML 템플릿 렌더링
        return render(request, 'index.html', {'map_html': map_html})
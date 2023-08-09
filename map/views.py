from django.shortcuts import render
from django.views import View
import folium

from tour_data.views import locationBasedList, searchFestivalList

class IndexMain(View):
    def get(self, request):
        latitude = 37.5665
        longitude = 126.9780
        # folium을 사용하여 지도 생성
        m = folium.Map(location=[latitude, longitude], zoom_start=12)

        # folium에 마커 추가
        dict = {"numOfRows":100}
        data = searchFestivalList(dict)
        if data["response"]["body"]["numOfRows"] > 0:
            FestivalList = data["response"]["body"]["items"]["item"]

        # 행사 마커 추가
        for Festival in FestivalList:
            folium.Marker(
                location=[Festival['mapy'],Festival['mapx']],
                popup=folium.Popup('<a href="/your-page-url">' + Festival['title'] + '</a>', max_width=100)
            ).add_to(m)


        # folium 지도를 HTML로 변환하여 템플릿에 전달
        map_html = m.get_root().render()

        # HTML 템플릿 렌더링
        return render(request, 'map.html', {'map_html': map_html})
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy, reverse
import folium

class Index(View):

    def get(self, request):
        # folium을 사용하여 지도 생성
        m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

        # folium에 마커 추가
        folium.Marker(location=[37.5665, 126.9780], popup='Seoul').add_to(m)

        # folium 지도를 HTML로 변환하여 템플릿에 전달
        map_html = m.get_root().render()

        # HTML 템플릿 렌더링
        return render(request, 'index.html', {'map_html': map_html})
from django.shortcuts import render
from django.views import View
from django.db.models import Q
from django.utils import timezone
from bs4 import BeautifulSoup
import folium

from tour_data.models import Event

current_date = timezone.now()

class IndexMain(View):
    def get(self, request):
        latitude = 37.5665
        longitude = 126.9780
        # folium을 사용하여 지도 생성
        m = folium.Map(location=[latitude, longitude], zoom_start=12)

        # folium에 마커 추가
        event = Event.objects.filter(Q(eventenddate__gt=current_date)).all().order_by('eventenddate')

        # 행사 마커 추가
        for Festival in event:
            folium.Marker(
                location=[Festival.mapy,Festival.mapx],
                popup=folium.Popup(f'<a href="/festival/detailview/{Festival.contentid}/{Festival.contenttypeid}">' + Festival.title + '</a>', max_width=100)
            ).add_to(m)


        # folium 지도를 HTML로 변환하여 템플릿에 전달
        map_html = m.get_root().render()

        soup = BeautifulSoup(map_html, 'html.parser')

        # 원하는 부분 선택 및 출력
        style_tag = soup.select('style')
        div_tag = soup.find('div', class_='folium-map')
        script_tag = soup.select('script')

        # 선택된 부분 출력
        context = {
            'style_tag':str(style_tag[-1]) if style_tag else None,
            'div_tag':str(div_tag),
            'script_tag':str(script_tag[-1]) if script_tag else None
        }

        # HTML 템플릿 렌더링
        return render(request, 'map.html', context)
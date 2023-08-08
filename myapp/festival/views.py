from django.shortcuts import render
from django.views import View

from tour_data.views import detailCommon
# Create your views here.
class DetailView(View):
    def get(self, request, contentid, contenttypeid):
        
        dict = {'contentid':contentid, 'contenttypeid':contenttypeid}
        data = detailCommon(dict)
        if data["response"]["body"]["numOfRows"] > 0:
            detail = data["response"]["body"]["items"]["item"]

        context = {
            'data': detail[0],
            'mapx': detail[0]['mapx'],
            'mapy': detail[0]['mapy'],
            }
        return render(request, 'detailview.html', context)
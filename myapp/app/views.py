from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View

from tour_data.views import searchFestivalList

class IndexMain(View):
    def get(self, request):
        data_list = {"item": []}

        data = searchFestivalList()
        if data["response"]["body"]["numOfRows"] > 0:
            for item in sorted(data["response"]["body"]["items"]["item"], key=lambda x: x['eventenddate']):
                data_list['item'].append(item)

        context = {'data': data_list}
        return render(request, 'index.html', context)
from django.shortcuts import render
from django.views import View
from django.utils import timezone
from datetime import datetime as dt
from datetime import timedelta

from tour_data.views import detailCommon
from .models import Festival

import logging
# Create your views here.

logger = logging.getLogger(__name__)
current_time = timezone.now()

def save_festival(data):
    try:
        contentid = data['contentid']

        createdtime = timezone.make_aware(dt.strptime(data['createdtime'], '%Y%m%d%H%M%S'))
        modifiedtime = timezone.make_aware(dt.strptime(data['modifiedtime'], '%Y%m%d%H%M%S'))

        defaults = {
            'contentid': data['contentid'],
            'contenttypeid': data['contenttypeid'],
            'title': data['title'],
            'createdtime': createdtime,
            'modifiedtime': modifiedtime,
            'tel': data['tel'],
            'telname': data['telname'],
            'homepage': data['homepage'],
            'booktour': data['booktour'],
            'firstimage': data['firstimage'],
            'firstimage2': data['firstimage2'],
            'cpyrhtDivCd': data['cpyrhtDivCd'],
            'areacode': data['areacode'],
            'sigungucode': data['sigungucode'],
            'cat1': data['cat1'],
            'cat2': data['cat2'],
            'cat3': data['cat3'],
            'addr1': data['addr1'],
            'addr2': data['addr2'],
            'zipcode': data.get('zipcode', ''),
            'mapx': data['mapx'],
            'mapy': data['mapy'],
            'mlevel': data['mlevel'],
            'overview': data['overview']
        }

        festival, created = Festival.objects.update_or_create(contentid=contentid, defaults=defaults)

        return festival
    except Exception as e:
        logger.error(f"Failed to save event(save_festival): {e}")
    

def check_festival(contentid):
    try:
        festival = Festival.objects.get(contentid=contentid)
        return festival
    except Festival.DoesNotExist:
        return None
    
class DetailView(View):
    def get(self, request, contentid, contenttypeid):
        festival = check_festival(contentid)
        if festival is None or (timezone.now() - festival.modifiedtime) >= timedelta(hours=1):
            dict = {'contentid':contentid, 'contenttypeid':contenttypeid}
            data = detailCommon(dict)
            if data["response"]["body"]["numOfRows"] > 0:
                detail = data["response"]["body"]["items"]["item"]
            
            festival = save_festival(detail[0])
        
        context = {
            'data': festival,
            'mapx': festival.mapx,
            'mapy': festival.mapy,
            }
        return render(request, 'detailview.html', context)
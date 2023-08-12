from django.http import JsonResponse
from django.conf import settings
from dotenv import load_dotenv
from django.utils import timezone
from datetime import datetime as dt
from django.db import transaction
from .models import Event
import os
import requests
import json
import logging
load_dotenv()
# Create your views here.
# 위치 기반 관광정보조회

logger = logging.getLogger(__name__)

serviceKey = os.getenv('serviceKey')

def parse_and_save_data(data):
    with transaction.atomic():
        for item in data['item']:
            try:
                contentid = item['contentid']

                defaults  = {
                    'addr1' : item['addr1'],
                    'addr2' : item['addr2'],
                    'booktour' : item['booktour'],
                    'cat1' : item['cat1'],
                    'cat2' : item['cat2'],
                    'cat3' : item['cat3'],
                    'contentid' : item['contentid'],
                    'contenttypeid' : item['contenttypeid'],
                    'createdtime' : timezone.make_aware(dt.strptime(item['createdtime'], '%Y%m%d%H%M%S')),
                    'eventstartdate' : dt.strptime(item['eventstartdate'], '%Y%m%d').date(),
                    'eventenddate' : dt.strptime(item['eventenddate'], '%Y%m%d').date(),
                    'firstimage' : item['firstimage'],
                    'firstimage2' : item['firstimage2'],
                    'cpyrhtDivCd' : item['cpyrhtDivCd'],
                    'mapx' : item['mapx'],
                    'mapy' : item['mapy'],
                    'mlevel' : item['mlevel'],
                    'modifiedtime' : timezone.make_aware(dt.strptime(item['modifiedtime'], '%Y%m%d%H%M%S')),
                    'areacode' : item['areacode'],
                    'sigungucode' : item['sigungucode'],
                    'tel' : item['tel'],
                    'title' : item['title']
                }
                event, created = Event.objects.update_or_create(
                    contentid=contentid,
                    defaults=defaults
                )
            except Exception as e:
                logger.error(f"Failed to save event(parse_and_save_data): {e}")


def locationBasedList(location):
    key = {'serviceKey':serviceKey, 'numOfRows':10 ,'pageNo':1,'MobileOS':'ETC','MobileApp':'Apptest','_type':'json','listYN':'Y','arrange':'C','mapX':location[1],'mapY':location[0],'radius':1000,'contentTypeId':15}
    url = 'http://apis.data.go.kr/B551011/KorService1/locationBasedList1?'

    for k, v in key.items():
        url += f'{k}={str(v)}&'

    response = requests.get(url)
    contents = json.loads(response.text)
    return contents

def searchFestivalList():
    pageNo = 1
    time = dt.now().strftime("%Y%m%d")
    key = {'serviceKey':serviceKey, 'numOfRows':100 ,'pageNo':pageNo,'MobileOS':'ETC','MobileApp':'Apptest','_type':'json','listYN':'Y','arrange':'Q','eventStartDate': time}
    url = 'http://apis.data.go.kr/B551011/KorService1/searchFestival1?'

    for k, v in key.items():
        url += f'{k}={str(v)}&'

    response = requests.get(url)
    data_list = {"item": []}
    data = json.loads(response.text)
    if data["response"]["body"]["numOfRows"] > 0:
        for item in sorted(data["response"]["body"]["items"]["item"], key=lambda x: x['eventenddate']):
            data_list['item'].append(item)
    with transaction.atomic():
        parse_and_save_data(data_list)

def loaderFestivalList(request):
    pageNo = 1
    data_list = {"item": []}
    if request.method == "GET":
        pageNo = request.GET.get("pageNo")
        time = dt.now().strftime("%Y%m%d")
        key = {'serviceKey':serviceKey, 'numOfRows':9 ,'pageNo':pageNo,'MobileOS':'ETC','MobileApp':'Apptest','_type':'json','listYN':'Y','arrange':'Q','eventStartDate': time}
        url = 'http://apis.data.go.kr/B551011/KorService1/searchFestival1?'

        for k, v in key.items():
            url += f'{k}={str(v)}&'

        response = requests.get(url)
        data = json.loads(response.text)
        if data["response"]["body"]["numOfRows"] > 0:
            for item in sorted(data["response"]["body"]["items"]["item"], key=lambda x: x['eventenddate']):
                data_list['item'].append(item)
        response_data = {
            "result": "success",
            "content": data_list,
            "message": "Data received",
        }
        return JsonResponse(response_data)

def tn_pubr_public_trrsrt_api(request):
    url = 'http://api.data.go.kr/openapi/tn_pubr_public_trrsrt_api'
    params ={'serviceKey' : 'AbbNHNXkmvK5lCExFYqhkaqIAo4XfqRyoG32doXNFbyqEQ79jtYo%2BKxPK0jK%2FwO81VMDcz3uQqNXeXgTiue%2BXg%3D%3D', 'pageNo' : '1', 'numOfRows' : '100', 'type' : 'json', 'trrsrtNm' : '', 'trrsrtSe' : '', 'rdnmadr' : '', 'lnmadr' : '', 'latitude' : '', 'longitude' : '', 'ar' : '', 'cnvnncFclty' : '', 'stayngInfo' : '', 'mvmAmsmtFclty' : '', 'recrtClturFclty' : '', 'hospitalityFclty' : '', 'sportFclty' : '', 'appnDate' : '', 'aceptncCo' : '', 'prkplceCo' : '', 'trrsrtIntrcn' : '', 'phoneNumber' : '', 'institutionNm' : '', 'referenceDate' : '', 'instt_code' : '' }

    for k, v in params.items():
        url += f'{k}={str(v)}&'

    response = requests.get(url)

    return JsonResponse(response.content)

def detailCommon(dict):
    pageNo = 1
    numOfRows = 10
    key = {'serviceKey':serviceKey, 'numOfRows': numOfRows ,'pageNo':pageNo,'MobileOS':'ETC','MobileApp':'Apptest','_type':'json','contentId':dict['contentid'],'contentTypeId': dict['contenttypeid'],'defaultYN': 'Y','firstImageYN': 'Y','areacodeYN': 'Y','catcodeYN': 'Y','addrinfoYN': 'Y','mapinfoYN': 'Y','overviewYN': 'Y',}
    url = 'http://apis.data.go.kr/B551011/KorService1/detailCommon1?'

    for k, v in key.items():
        url += f'{k}={str(v)}&'

    response = requests.get(url)
    contents = {}
    if(response):
        contents = json.loads(response.text)
    return contents
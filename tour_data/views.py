from django.http import JsonResponse
from django.conf import settings
from dotenv import load_dotenv
import os
import requests
import json
import datetime

load_dotenv()
# Create your views here.
# 위치 기반 관광정보조회

serviceKey = os.getenv('serviceKey')
def locationBasedList(location):
    key = {'serviceKey':serviceKey, 'numOfRows':10 ,'pageNo':1,'MobileOS':'ETC','MobileApp':'Apptest','_type':'json','listYN':'Y','arrange':'C','mapX':location[1],'mapY':location[0],'radius':1000,'contentTypeId':15}
    url = 'http://apis.data.go.kr/B551011/KorService1/locationBasedList1?'

    for k, v in key.items():
        url += f'{k}={str(v)}&'

    response = requests.get(url)
    contents = json.loads(response.text)
    return contents

def searchFestivalList(dict):
    pageNo = 1
    time = datetime.datetime.now().strftime("%Y%m%d")
    key = {'serviceKey':serviceKey, 'numOfRows':dict['numOfRows'] ,'pageNo':pageNo,'MobileOS':'ETC','MobileApp':'Apptest','_type':'json','listYN':'Y','arrange':'Q','eventStartDate': time}
    url = 'http://apis.data.go.kr/B551011/KorService1/searchFestival1?'

    for k, v in key.items():
        url += f'{k}={str(v)}&'

    response = requests.get(url)
    contents = json.loads(response.text)
    return contents

def loaderFestivalList(request):
    pageNo = 1
    data_list = {"item": []}
    if request.method == "GET":
        pageNo = request.GET.get("pageNo")
        time = datetime.datetime.now().strftime("%Y%m%d")
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
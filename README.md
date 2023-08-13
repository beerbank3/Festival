# 개요  
전국 축제 일정 데이터를 활용한 Django Project

# 목표  
- 공공데이터 API를 사용하여 API 사용경험  
- Django에 대한 숙련도 증가  
- 오류 발생시 오류 처리 경험 
- 프로젝트 초기부터 완성까지 스스로 해보는 경험  

# 기능  


# ERD


# 페이지 사진
- 메인
![Alt text](/README/main.png)
- 지도
![Alt text](/README/map.png)

# 동작방식 변경

1. API 데이터 조회방식변경

- API조회후 데이터 표출 -> 일정시간 지난후, 특정조건 발생시 DB에 추가하는방식

- 이유: 기존방식 사용시 1일 사용횟수 1000회를 초과하는 상황 발생가능


# 에러 발생
1. 서버 실행시 **database is locked** 자주 발생  

- 해당코드는 축제 정보를 10분에 100개씩 정보가있으면 update없으면 create
```
event, created = Event.objects.update_or_create(
    contentid=contentid,
    defaults=defaults
)
```
- 이 코드에서 에러가 발생하는것으로 예상

```
try:
    event = Event.objects.get(contentid=contentid)
    for field, value in defaults.items():
        setattr(event, field, value)  # 필드 업데이트
    with transaction.atomic():
        event.save()

except ObjectDoesNotExist:
    event = Event(contentid=contentid, **defaults)
    with transaction.atomic():
        event.save()
```
- update_or_create()을 안쓰는것으로 동작방식 변경

- 현재는 에러 발생 X(에러 재발생시 100개 -> 50개씩으로  분할 예정)

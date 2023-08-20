# 개요  
전국 축제 일정 데이터를 활용한 Django Project

# 목표  
- 공공데이터 API 사용 경험  
- Django 숙련도 향상  
- 오류 처리 경험  
- 프로젝트 완성 경험    

# 기능  
1. 전국 축제 List
- 이 기능은 전국적으로 열리는 다양한 축제의 목록을 표시하는 기능입니다. 이 기능을 통해 사용자는 축제의 이름, 날짜, 장소 등의 기본 정보를 확인할 수 있습니다.

2. 지도로 보는 전국 축제 위치
- 이 기능은 축제의 위치를 지도 상에 표시하는 기능입니다. 사용자는 지도를 통해 각 축제의 위치를 파악할수있습니다.


# ERD
       +--------------------------+         +--------------------------+
       |        Festival          |         |          Event           |
       +--------------------------+         +--------------------------+
       | contentid (PK)           |         | contentid (PK)           |
       | contenttypeid            |         | contenttypeid            |
       | title                    |         | title                    |
       | createdtime              |         | createdtime              |
       | modifiedtime             |         | eventstartdate           |
       | tel                      |         | eventenddate             |
       | telname                  |         | addr1                    |
       | homepage                 |         | addr2                    |
       | booktour                 |         | booktour                 |
       | firstimage               |         | cat1                     |
       | firstimage2              |         | cat2                     |
       | cpyrhtDivCd              |         | cat3                     |
       | areacode                 |         | mapx                     |
       | sigungucode              |         | mapy                     |
       | cat1                     |         | mlevel                   |
       | cat2                     |         | modifiedtime             |
       | cat3                     |         | areacode                 |
       | addr1                    |         | sigungucode              |
       | addr2                    |         | tel                      |
       | zipcode                  |         +--------------------------+
       | mapx                     |
       | mapy                     |
       | mlevel                   |
       | overview                 |
       +--------------------------+

# 페이지 사진
- **메인**  
![Alt text](/README/main.png)
- **지도**  
![Alt text](/README/map.png)
![Alt text](/README/map_1.png)
- **상세페이지**  
![Alt text](/README/detail.png)

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

# 결과
1. 공공데이터 API 사용 경험  
- 목표: 축제 데이터 API를 사용하며 API 활용 경험을 쌓는 것이었습니다.
- 성과: 축제 데이터 API를 활용하여 다양한 축제 정보를 검색하고 표시하는 기능을 구현하면서 API 사용에 익숙해졌습니다. 또한, 1일 사용 한도가 있는 API를 다루면서 API 요청을 최적화하고 효율적으로 사용하는 방법을 배우게 되었습니다. 예를 들어 동일한 요청을 반복하지 않고 필요한 정보를 더욱 빠르게 가져올 수 있는 방법을 고민하게 되었습니다.

2. Django 숙련도 향상  
- 목표: Django를 사용하여 프로젝트를 진행하며 프레임워크에 대한 이해와 숙련도를 향상시키는 것이었습니다.
- 성과: 프로젝트를 진행하면서 Django의 기본 구조와 흐름을 더 깊이 이해하게 되었습니다. 특히, 프로젝트를 중단하고 다시 진행하면서 폴더 구조와 템플릿, 정적 파일의 위치에 대한 중요성을 깨달았습니다. 프로젝트 구조를 재조정하며 코드의 유지보수성을 향상시키는 방법에 대한 고민을 하게 되었습니다.

3. 오류 처리 경험  
- 목표: 다양한 상황에서 발생하는 오류들을 경험하며 빠르게 문제를 해결하는 방법을 습득하는 것이었습니다.
- 성과: 프로젝트 진행 중 다양한 오류들을 마주하면서 문제 해결 능력이 향상되었습니다. 오류 메시지를 이해하고 해당 오류를 해결하기 위한 검색과 디버깅 기술을 연마하게 되었습니다. 또한, 이전에 경험하지 못한 예상치 못한 문제에 대처하면서 창의적인 문제 해결 방법을 생각해보는 능력도 향상시켰습니다.

4. 프로젝트 완성 경험
- 목표: 프로젝트를 초기부터 완성까지 스스로 진행하며 전체적인 경험을 쌓는 것이었습니다.
- 성과: 이번 프로젝트에서 목표를 완전히 달성하지는 못했지만, 프로젝트를 시작하고 진행하는 과정을 통해 많은 것을 배웠습니다. 초기에 잡았던 기능을 구현하지 못했더라도, 프로젝트 관리와 계획 수립, 어려움을 극복하는 능력을 강화할 수 있는 기회였습니다. 이번 프로젝트에서 배운 교훈을 다음 프로젝트에 적용하여 더 나은 결과물을 만들어보고자 합니다.
# 개요  
전국 축제 일정 데이터를 활용한 Django Project

# 목표  
- 공공데이터 API를 사용하여 API 사용경험  
- Django에 대한 숙련도 증가  
- 오류 발생시 오류 처리 경험 
- 프로젝트 초기부터 완성까지 스스로 해보는 경험  

# 기능  


# ERD


# 동작방식 변경

1. API 데이터 조회방식변경

- API조회후 데이터 표출 -> 일정시간 지난후, 특정조건 발생시 DB에 추가하는방식

- 이유: 기존방식 사용시 1일 사용횟수 1000회를 초과하는 상황 발생가능


# 에러 발생
- 서버 시작시 **database is locked** 발생

- 서버시작시 searchFestivalList()를 백그라운드에서 진행하면서 트랙잭션 관리가 안된거같음

```
with transaction.atomic():
```
- 코드를 searchFestivalList()와 parse_and_save_data(data):함수에 추가
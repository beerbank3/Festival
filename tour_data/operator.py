from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from .views import searchFestivalList


def my_task():
    # 작업 내용을 여기에 작성
    searchFestivalList()
    pass

scheduler = BackgroundScheduler(job_defaults={'max_instances': 2})
#scheduler.add_job(my_task, IntervalTrigger(seconds=10))
scheduler.add_job(my_task, CronTrigger.from_crontab('*/10 * * * *'))  # 매 10분마다 실행

scheduler.start()
from django.apps import AppConfig
from django.conf import settings

class TourDataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tour_data'

    def ready(self):
        if settings.SCHEDULER_DEFAULT:
            from . import operator
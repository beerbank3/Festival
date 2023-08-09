from django.urls import path
from . import views

app_name = 'tour_data'

urlpatterns = [
    path('loaderFestivalList/', views.loaderFestivalList, name='loaderFestivalList'),
]
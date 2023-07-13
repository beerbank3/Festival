from django.urls import path
from . import views

app_name = 'festival'

urlpatterns = [
    path('detailview/<int:contentid>/<int:contenttypeid>', views.DetailView.as_view(), name='detailview'),
]
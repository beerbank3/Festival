from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.db.models import Q
from django.utils import timezone

from tour_data.models import Event

current_date = timezone.now()

class IndexMain(View):
    def get(self, request):
        events = Event.objects.filter(Q(eventenddate__gt=current_date)).all().order_by('eventenddate')
        context = {'data': events}
        return render(request, 'index.html', context)
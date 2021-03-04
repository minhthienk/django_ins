from django.shortcuts import render
from django.http import HttpResponse

from .models import ScheduleFile


# Create your views here.
def schedule(request):
    return render(request = request,
                  template_name='schedule/schedule_list.html',
                  context = {'schedules':ScheduleFile.objects.all})
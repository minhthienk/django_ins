
from django.shortcuts import render
from django_tables2 import SingleTableView
from .models import WeekSchedule
from .tables import WeekScheduleTable

from django.forms.models import model_to_dict



def week_schedule_view(request):
    schedule_data = WeekSchedule.objects.all()

    instance = WeekSchedule.objects.get(id=1)
    instance.mon = '<span style="color: red">test text but \nthis section is red</span>'
    instance.save()
    #schedule_data = WeekSchedule.objects.all()
    return render(request, 'schedule/week_schedule.html', {'table': schedule_data})


def put_teacher_schedule(schedule_data):
    teachers = {'teacher A':'planned',
                'teacher B':'available'}

    instance = WeekSchedule.objects.get(id=1)
    instance.mon = 'how are you'  # change field
    instance.save()


class WeekScheduleView(SingleTableView):
    model = WeekSchedule
    table_class = WeekScheduleTable
    template_name = 'schedule/week_schedule.html'

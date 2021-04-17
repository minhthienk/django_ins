import django_tables2 as tables
from .models import WeekSchedule




class WeekScheduleTable(tables.Table):
    class Meta:
        model = WeekSchedule
        template_name = "django_tables2/bootstrap4.html"
        fields = ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')
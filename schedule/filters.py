

'''
from django import forms
from .models import WeekSchedule
import django_filters

class WeekScheduleFilter(django_filters.FilterSet):

    class Meta:
        model = WeekSchedule
        #fields = ['username', 'first_name', 'last_name', ]
        fields = ['username', 'first_name', 'last_name']'''
from django.contrib import admin
from .models import ScheduleFile


# Register your models here.



class ScheduleFileAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title']

admin.site.register(ScheduleFile, ScheduleFileAdmin)
from django.db import models

# Create your models here.
'''
class AllSchedule(models.Model):
    """docstring for AllSchedule"""
    week_num = models.CharField(max_length=100, verbose_name="Week")
'''
class WeekSchedule(models.Model):
    mon = models.CharField(max_length=100, verbose_name="Mon")
    tue = models.CharField(max_length=100, verbose_name="Tue")
    wed = models.CharField(max_length=100, verbose_name="Wed")
    thu = models.CharField(max_length=100, verbose_name="Thu")
    fri = models.CharField(max_length=100, verbose_name="Fri")
    sat = models.CharField(max_length=100, verbose_name="Sat")
    sun = models.CharField(max_length=100, verbose_name="Sun")
    #week_schedule = models.ForeignKey(AllSchedule, on_delete=models.CASCADE)


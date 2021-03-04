from django.db import models

# Create your models here.


class ScheduleFile(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField('Schedule file', upload_to='', null=True, blank=True)

    def __str__(self):
        return self.title



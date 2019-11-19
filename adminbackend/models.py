from django.db import models
import requests
from datetime import datetime


# Create your models here.
class HomePageProject(models.Model):
    event_name = models.CharField(max_length=200)
    event_description = models.CharField(max_length=250)
    event_image = models.ImageField(upload_to='project_image/homepage/%Y/%m/%d/', null=True, blank=True)
    event_place = models.CharField(max_length=250)
    event_time = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.event_name


class HomeContactForm(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    email = models.EmailField()
    time = models.TimeField()
    phone = models.IntegerField()
    people = models.CharField(max_length=200)
    message = models.CharField(max_length=300)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.email

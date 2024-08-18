import datetime
from django.db import models

class Post(models.Model):
    tittle = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images')
    date = models.DateTimeField(datetime.date.today)

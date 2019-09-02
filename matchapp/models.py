from django.db import models

# Create your models here.

class TennisModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    date = models.CharField(max_length=100, null=True)
#    date1 = models.DateField(null=True)
    time = models.CharField(max_length=100, null=True)
    place = models.CharField(max_length=100, null=True)

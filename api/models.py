from django.db import models


# Create your models here.

class ExampleModel(models.Model):
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=30)
    degree = models.CharField(max_length=30)
    place = models.IntegerField()
    date = models.CharField(max_length=30)

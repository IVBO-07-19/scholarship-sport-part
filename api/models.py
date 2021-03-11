from django.db import models


# Create your models here.

class ExampleModel(models.Model):
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=30)
    degree = models.CharField(max_length=30)
    place = models.IntegerField()
    date = models.CharField(max_length=30)


class Table1(models.Model):
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=30)
    degree = models.CharField(max_length=30)
    place = models.IntegerField()
    date = models.DateField()
    points = models.IntegerField()


class Table2(models.Model):
    trp_badge = models.BooleanField()
    date = models.DateField()
    age_group = models.IntegerField()
    points = models.IntegerField()


class Table3(models.Model):
    name = models.CharField(max_length=200)
    degree = models.CharField(max_length=30)
    date = models.DateField()
    points = models.IntegerField()


class Table4(models.Model):
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=30)
    degree = models.CharField(max_length=30)
    date = models.DateField()
    points = models.IntegerField()


class Table5(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    points = models.IntegerField()


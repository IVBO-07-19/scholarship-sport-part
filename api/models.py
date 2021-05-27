from django.db import models
from django.core.exceptions import ValidationError
# Validators


def level_validator(level):
    if level.lower() not in ("международное", "всероссийское", "региональное", "ведомственное"):
        raise ValidationError(
            f"'{level}' is an inappropriate value!",
            params={"level": level},
        )


def degree_validator(degree):
    if degree.lower() not in ("индивидуальное", "командное"):
        raise ValidationError(
            f"'{degree}' is an inappropriate value!",
            params={"degree": degree},
        )


def age_group_validator(age_group):
    if not 1 <= age_group <= 11:
        raise ValidationError(
            f"'{age_group}' is an inappropriate value!",
            params={"age_group": age_group},
        )

def place_validator(place):
    if place < 1:
        raise ValidationError(
            f"Place must be greater than 0!",
            params={"place": place},
        )


class GlobalEvent(models.Model):
    requestID = models.CharField(max_length=64, default=0)
    userID = models.CharField(max_length=64, null=True)
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=30, validators=[level_validator])
    degree = models.CharField(max_length=30, validators=[degree_validator])
    place = models.IntegerField(validators=[place_validator])
    date = models.DateField()
    points = models.IntegerField(blank=True, null=True)




class TRPBadge(models.Model):
    requestID = models.CharField(max_length=64, default=0)
    userID = models.CharField(max_length=64, blank=False)
    trp_badge = models.BooleanField()
    date = models.DateField()
    age_group = models.IntegerField(validators=[age_group_validator])
    points = models.IntegerField()


class NationalPart(models.Model):
    requestID = models.CharField(max_length=64, default=0)
    userID = models.CharField(max_length=64, blank=False)
    name = models.CharField(max_length=200)
    degree = models.CharField(max_length=30, validators=[degree_validator])
    date = models.DateField()
    points = models.IntegerField()


class NotNationalPart(models.Model):
    requestID = models.CharField(max_length=64, default=0)
    userID = models.CharField(max_length=64, blank=False)
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=30, validators=[level_validator])
    degree = models.CharField(max_length=30,validators=[degree_validator])
    date = models.DateField()
    points = models.IntegerField()


class Online(models.Model):
    requestID = models.CharField(max_length=64, default=0)
    userID = models.CharField(max_length=64, blank=False)
    name = models.CharField(max_length=200)
    date = models.DateField()
    points = models.IntegerField()






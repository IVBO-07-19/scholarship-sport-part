# Generated by Django 3.1.7 on 2021-04-08 14:00

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210408_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalevent',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='globalevent',
            name='degree',
            field=models.CharField(max_length=30, validators=[api.models.degree_validator]),
        ),
        migrations.AlterField(
            model_name='notnationalpart',
            name='degree',
            field=models.CharField(max_length=30, validators=[api.models.degree_validator]),
        ),
        migrations.AlterField(
            model_name='notnationalpart',
            name='level',
            field=models.CharField(max_length=30, validators=[api.models.level_validator]),
        ),
        migrations.AlterField(
            model_name='trpbadge',
            name='age_group',
            field=models.IntegerField(validators=[api.models.age_group_validator]),
        ),
    ]
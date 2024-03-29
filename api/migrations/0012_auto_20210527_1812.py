# Generated by Django 3.1.7 on 2021-05-27 15:12

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20210507_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalevent',
            name='place',
            field=models.IntegerField(validators=[api.models.place_validator]),
        ),
        migrations.AlterField(
            model_name='nationalpart',
            name='degree',
            field=models.CharField(max_length=30, validators=[api.models.degree_validator]),
        ),
        migrations.AlterField(
            model_name='nationalpart',
            name='points',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='nationalpart',
            name='userID',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='notnationalpart',
            name='points',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='notnationalpart',
            name='userID',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='online',
            name='points',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='online',
            name='userID',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='trpbadge',
            name='points',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='trpbadge',
            name='userID',
            field=models.CharField(max_length=64, null=True),
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-08 13:45

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210325_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalevent',
            name='level',
            field=models.CharField(max_length=30, validators=[api.models.level_validator]),
        ),
    ]

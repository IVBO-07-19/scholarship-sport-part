# Generated by Django 3.1.7 on 2021-04-22 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210422_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalevent',
            name='userID',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='nationalpart',
            name='userID',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='notnationalpart',
            name='userID',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='online',
            name='userID',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='trpbadge',
            name='userID',
            field=models.CharField(max_length=64),
        ),
    ]
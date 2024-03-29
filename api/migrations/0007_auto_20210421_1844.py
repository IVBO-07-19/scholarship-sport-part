# Generated by Django 3.1.7 on 2021-04-21 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210408_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalevent',
            name='userID',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nationalpart',
            name='userID',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notnationalpart',
            name='userID',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='online',
            name='userID',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trpbadge',
            name='userID',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
    ]

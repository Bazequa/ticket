# Generated by Django 4.1.3 on 2022-12-08 07:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketingtoolapp', '0009_applicationmodel_request_raised_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationarymodel',
            name='request_raised_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]

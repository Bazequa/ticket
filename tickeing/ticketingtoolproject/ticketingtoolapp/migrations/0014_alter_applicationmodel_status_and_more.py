# Generated by Django 4.1.3 on 2022-12-09 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketingtoolapp', '0013_applicationmodel_status_bookingmodel_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationmodel',
            name='status',
            field=models.CharField(choices=[('raised', 'raised'), ('accept', 'accept'), ('reject', 'reject'), ('complete', 'complete')], default='raised', editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='bookingmodel',
            name='status',
            field=models.CharField(choices=[('raised', 'raised'), ('accept', 'accept'), ('reject', 'reject'), ('complete', 'complete')], default='raised', editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='status',
            field=models.CharField(choices=[('raised', 'raised'), ('accept', 'accept'), ('reject', 'reject'), ('complete', 'complete')], default='raised', editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='stationarymodel',
            name='status',
            field=models.CharField(choices=[('raised', 'raised'), ('accept', 'accept'), ('reject', 'reject'), ('complete', 'complete')], default='raised', editable=False, max_length=100),
        ),
    ]

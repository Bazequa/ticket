# Generated by Django 4.1.3 on 2022-12-19 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketingtoolapp', '0021_ticket_status_alter_ticket_ticket_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_no',
            field=models.CharField(default='OJ-17G4D0', max_length=10, unique=True),
        ),
    ]

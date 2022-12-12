# Generated by Django 4.1.3 on 2022-12-12 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketingtoolapp', '0020_ticket_request_raised_at_alter_ticket_ticket_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='Status',
            field=models.CharField(choices=[('raised', 'raised'), ('accepted', 'accepted'), ('rejected', 'rejected'), ('completed', 'completed')], default='raised', max_length=100),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_no',
            field=models.CharField(default='OJ-XK0NJ4', max_length=10, unique=True),
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-20 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketingtoolapp', '0024_ticket_comment_alter_ticket_ticket_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_no',
            field=models.CharField(default='OJ-4HPON3', max_length=10, unique=True),
        ),
    ]

# Generated by Django 2.2.16 on 2020-10-31 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_event_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(default='', max_length=100, unique=True, verbose_name='Event Name'),
        ),
    ]

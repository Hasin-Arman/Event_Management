# Generated by Django 4.2.3 on 2023-11-27 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='registered',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
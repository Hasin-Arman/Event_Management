# Generated by Django 4.2.3 on 2023-11-28 07:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0008_event_registered_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event_registration',
            name='user',
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]

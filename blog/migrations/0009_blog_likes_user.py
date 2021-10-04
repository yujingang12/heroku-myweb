# Generated by Django 3.2.7 on 2021-10-03 06:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_auto_20210927_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='likes_user',
            field=models.ManyToManyField(blank=True, related_name='likes_user', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 3.2 on 2021-09-27 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210927_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='username',
        ),
        migrations.AddField(
            model_name='comment',
            name='pub_date',
            field=models.DateField(null=True, verbose_name='date published'),
        ),
    ]

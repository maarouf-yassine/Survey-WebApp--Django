# Generated by Django 3.2 on 2021-04-08 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveyapp', '0006_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='points',
        ),
    ]

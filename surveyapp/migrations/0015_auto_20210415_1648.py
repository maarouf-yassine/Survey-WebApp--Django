# Generated by Django 3.1.6 on 2021-04-15 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveyapp', '0014_auto_20210415_1647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='survey',
            old_name='choice1',
            new_name='agree',
        ),
        migrations.RenameField(
            model_name='survey',
            old_name='choice2',
            new_name='disagree',
        ),
        migrations.RenameField(
            model_name='survey',
            old_name='choice3',
            new_name='neutral',
        ),
        migrations.RenameField(
            model_name='survey',
            old_name='choice4',
            new_name='stronglyagree',
        ),
        migrations.AddField(
            model_name='survey',
            name='stronglydisagree',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-21 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0030_choice_question_submission_survey_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='participant_email',
        ),
    ]

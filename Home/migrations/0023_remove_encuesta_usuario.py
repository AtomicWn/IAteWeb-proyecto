# Generated by Django 4.1.3 on 2022-11-21 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0022_remove_question_survey_remove_submission_answer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encuesta',
            name='usuario',
        ),
    ]
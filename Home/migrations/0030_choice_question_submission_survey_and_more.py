# Generated by Django 4.1.3 on 2022-11-21 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0029_datos_importantes_encuesta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_email', models.EmailField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('answer', models.ManyToManyField(to='Home.choice')),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='pregunta',
            name='encuesta',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='pregunta',
        ),
        migrations.RemoveField(
            model_name='respuesta_usuario',
            name='contesta',
        ),
        migrations.RemoveField(
            model_name='respuesta_usuario',
            name='encuesta',
        ),
        migrations.DeleteModel(
            name='datos_importantes',
        ),
        migrations.DeleteModel(
            name='encuesta',
        ),
        migrations.DeleteModel(
            name='pregunta',
        ),
        migrations.DeleteModel(
            name='respuesta',
        ),
        migrations.DeleteModel(
            name='respuesta_usuario',
        ),
        migrations.AddField(
            model_name='submission',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Home.survey'),
        ),
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Home.survey'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.question'),
        ),
    ]
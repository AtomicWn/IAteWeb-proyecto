# Generated by Django 4.1.3 on 2022-11-21 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0024_rename_texto_pregunta_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='respuesta_usuario',
            old_name='respuesta',
            new_name='contesta',
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='encuesta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Home.encuesta'),
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='pregunta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.pregunta'),
        ),
        migrations.AlterField(
            model_name='respuesta_usuario',
            name='encuesta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Home.encuesta'),
        ),
    ]

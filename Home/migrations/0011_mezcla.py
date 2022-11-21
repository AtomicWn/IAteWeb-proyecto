# Generated by Django 4.1.3 on 2022-11-20 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_delete_submana'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mezcla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Home.choice')),
                ('subido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Home.submission')),
            ],
        ),
    ]

# Generated by Django 3.0.2 on 2020-04-21 16:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volumechange', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)])),
                ('panningposition', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)], verbose_name='Position of an instrument/vocal in stereo field')),
                ('additionalcomments', models.TextField(blank=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracks.Project')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracks.Track')),
            ],
        ),
    ]

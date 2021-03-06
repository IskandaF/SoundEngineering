# Generated by Django 3.0.2 on 2020-04-21 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tracks.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name of the project')),
                ('uploadfile', models.FileField(upload_to=tracks.models.user_directory_path)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name of the track')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracks.Project')),
            ],
        ),
    ]

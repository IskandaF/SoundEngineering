# Generated by Django 3.0.2 on 2020-04-21 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='user',
            new_name='user_id',
        ),
    ]
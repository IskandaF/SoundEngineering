# Generated by Django 3.0.2 on 2020-05-22 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineer',
            name='vkid',
            field=models.CharField(max_length=32),
        ),
    ]

# Generated by Django 2.0.3 on 2018-09-24 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
    ]
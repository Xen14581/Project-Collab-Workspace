# Generated by Django 3.0.5 on 2021-04-21 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='title',
        ),
    ]

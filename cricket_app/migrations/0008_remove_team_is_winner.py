# Generated by Django 4.1.13 on 2023-11-26 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cricket_app', '0007_team_is_winner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='is_winner',
        ),
    ]

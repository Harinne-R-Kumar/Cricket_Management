# Generated by Django 4.1.13 on 2023-11-26 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket_app', '0006_teampoints'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='is_winner',
            field=models.BooleanField(default=False),
        ),
    ]

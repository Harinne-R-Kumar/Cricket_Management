# Generated by Django 4.1.13 on 2023-11-26 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket_app', '0003_match'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointsTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=100, unique=True)),
                ('matches_played', models.PositiveIntegerField(default=0)),
                ('matches_won', models.PositiveIntegerField(default=0)),
                ('matches_lost', models.PositiveIntegerField(default=0)),
                ('matches_drawn', models.PositiveIntegerField(default=0)),
                ('points', models.PositiveIntegerField(default=0)),
                ('runs_scored', models.PositiveIntegerField(default=0)),
                ('wickets_taken', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
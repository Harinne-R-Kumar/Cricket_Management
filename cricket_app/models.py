# cricket_management/cricket_app/models.py

from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='team_logos/', null=True, blank=True)
    def __str__(self):
        return self.name
class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Match(models.Model):
    # Define your Match model fields here
    # For example:
    date = models.DateField()
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1_matches')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2_matches')
    result = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.team1} vs {self.team2} on {self.date}"

class TeamPoints(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE, primary_key=True)
    matches_played = models.PositiveIntegerField(default=0)
    matches_won = models.PositiveIntegerField(default=0)
    matches_lost = models.PositiveIntegerField(default=0)
    matches_drawn = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.team.name
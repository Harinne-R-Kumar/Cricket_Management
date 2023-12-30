# cricket_management/cricket_app/forms.py

from django import forms
from .models import Team,Player,Match

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name','logo']
class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['team', 'name', 'role']


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['date', 'team1', 'team2', 'result']

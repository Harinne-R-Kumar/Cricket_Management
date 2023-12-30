# cricket_management/cricket_app/views.py

from django.shortcuts import render
# cricket_management/cricket_app/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib import messages
from .models import Team,Player,Match
from .forms import TeamForm,PlayerForm,MatchForm


points_table_data = [
            {'team': 'India', 'matches_played': 9, 'matches_won': 9, 'matches_lost': 0, 'matches_drawn': 0,
             'points': 18,'logo': 'india_logo.jpg'},
            {'team': 'South Africa', 'matches_played': 9, 'matches_won': 7, 'matches_lost': 2, 'matches_drawn': 0,
             'points': 14,'logo': 'south_africa_logo.jpg'},
            {'team': 'Australia', 'matches_played': 9, 'matches_won': 7, 'matches_lost': 2, 'matches_drawn': 0,
             'points': 14,'logo': 'australia_logo.jpg'},
            {'team': 'New Zealand', 'matches_played': 9, 'matches_won': 5, 'matches_lost': 4, 'matches_drawn': 0,
             'points': 10, 'logo': 'new_zealand_logo.jpg'},
            {'team': 'pakistan', 'matches_played': 9, 'matches_won': 4, 'matches_lost': 5, 'matches_drawn': 0,
             'points': 8, 'logo': 'pakistan_logo.jpg'},
            {'team': 'Afghanistan', 'matches_played': 9, 'matches_won': 7, 'matches_lost': 2, 'matches_drawn': 0,
             'points': 14, 'logo': 'afghanistan_logo.jpg'},
            {'team': 'England', 'matches_played': 9, 'matches_won': 3, 'matches_lost': 6, 'matches_drawn': 0,
             'points': 14, 'logo': 'england_logo.jpg'},
            {'team': 'Bangladesh', 'matches_played': 9, 'matches_won': 2, 'matches_lost': 7, 'matches_drawn': 0,
             'points': 14, 'logo': 'bangladesh_logo.jpg'},
            {'team': 'Sri Lanka', 'matches_played': 9, 'matches_won': 2, 'matches_lost': 7, 'matches_drawn': 0,
             'points': 14, 'logo': 'srilanka_logo.jpg'},
            {'team': 'Netherlands', 'matches_played': 9, 'matches_won': 2, 'matches_lost': 7, 'matches_drawn': 0,
             'points': 14, 'logo': 'netherlands_logo.jpg'},
    # ... (other data)
        ]

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'team_list.html', {'teams': teams})

def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    return render(request, 'team_detail.html', {'team': team})

def team_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            team = form.save()
            return redirect('team_detail', pk=team.pk)
    else:
        form = TeamForm()
    return render(request, 'team_form.html', {'form': form})

def team_edit(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            team = form.save()
            return redirect('team_detail', pk=team.pk)
    else:
        form = TeamForm(instance=team)
    return render(request, 'team_form.html', {'form': form})

def team_delete(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        team.delete()
        return redirect('team_list')
    return render(request, 'team_confirm_delete.html', {'object': team})
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            messages.success(request, f'Welcome, {username}! You have successfully logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    return render(request, 'login.html')
def registration(request):
    return render(request, 'registration.html')

def logout(request):
    django_logout(request)  # Use Django's built-in logout function
    return render(request, 'logout.html')
def points_table(request):
        return render(request, 'points_table.html', {'points_table_data': points_table_data})
def update_points(request, team_name):
    # Access points_table_data at the module level
    global points_table_data

    # Dummy function to simulate updating points when a team wins a match
    # You should replace this with your actual logic for updating points based on match results
    # For demonstration purposes, this function simply adds 2 points to the team's total

    # Find the team in the points table data
    for team in points_table_data:
        if team['team'] == team_name:
            # Update points
            team['points'] += 2
            team['matches_played']+=1
            team['matches_won']+=1

    # Redirect back to the points table page after updating
    return redirect('points_table')
def match_list(request):
    matches = Match.objects.all()
    return render(request, 'match_list.html', {'matches': matches})

def match_detail(request, pk):
    match = get_object_or_404(Match, pk=pk)
    return render(request, 'match_detail.html', {'match': match})

def match_create(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            match = form.save()
            return redirect('match_detail', pk=match.pk)
    else:
        form = MatchForm()
    return render(request, 'match_form.html', {'form': form})

def match_edit(request, pk):
    match = get_object_or_404(Match, pk=pk)
    if request.method == 'POST':
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            match = form.save()
            return redirect('match_detail', pk=match.pk)
    else:
        form = MatchForm(instance=match)
    return render(request, 'match_form.html', {'form': form})

def match_delete(request, pk):
    match = get_object_or_404(Match, pk=pk)
    if request.method == 'POST':
        match.delete()
        return redirect('match_list')
    return render(request, 'match_confirm_delete.html', {'object': match})
def player_list(request):
    players = Player.objects.all()
    return render(request, 'player_list.html', {'players': players})

def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'player_detail.html', {'player': player})

def player_create(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save()
            return redirect('player_detail', pk=player.pk)
    else:
        form = PlayerForm()
    return render(request, 'player_form.html', {'form': form})

def player_edit(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            player = form.save()
            return redirect('player_detail', pk=player.pk)
    else:
        form = PlayerForm(instance=player)
    return render(request, 'player_form.html', {'form': form})

def player_delete(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        player.delete()
        return redirect('player_list')
    return render(request, 'player_confirm_delete.html', {'object': player})

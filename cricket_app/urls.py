# cricket_management/cricket_app/urls.py
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.urls import path
from .views import home, login, points_table, team_list, team_detail, team_create, team_edit, team_delete,player_list, player_detail, player_create, player_edit, player_delete,update_points,registration,logout,match_list,match_detail,match_create,match_edit,match_delete


urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('logout/', logout, name='logout'),
    path('points_table/', points_table, name='points_table'),
    path('update_points/<str:team_name>/', update_points, name='update_points'),
    path('matches/', views.match_list, name='match_list'),
    path('matches/create/', views.match_create, name='match_create'),
    path('matches/<int:pk>/', views.match_detail, name='match_detail'),
    path('matches/<int:pk>/edit/', views.match_edit, name='match_edit'),
    path('matches/<int:pk>/delete/', views.match_delete, name='match_delete'),
    path('teams/', team_list, name='team_list'),
    path('teams/<int:pk>/', team_detail, name='team_detail'),
    path('teams/new/', team_create, name='team_create'),
    path('teams/<int:pk>/edit/', team_edit, name='team_edit'),
    path('teams/<int:pk>/delete/', team_delete, name='team_delete'),
    path('players/', player_list, name='player_list'),
    path('players/<int:pk>/', player_detail, name='player_detail'),
    path('players/new/', player_create, name='player_create'),
    path('players/<int:pk>/edit/', player_edit, name='player_edit'),
    path('players/<int:pk>/delete/', player_delete, name='player_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
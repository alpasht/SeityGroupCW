from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Teams related URLs
    path('teams/', views.teams, name='teams'),
    path('teams/create/', views.team_create, name='team_create'),
    path('teams/<int:id>/', views.team_detail, name='team_detail'),
    
    # Placeholder URLs
    path('dashboard/', views.dummy_view, name='dashboard'),
    path('organisation/', views.dummy_view, name='organisation'),
    path('messages/', views.dummy_view, name='messages'),
    path('schedule/', views.dummy_view, name='schedule'),
]
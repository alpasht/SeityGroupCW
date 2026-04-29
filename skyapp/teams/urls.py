from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Teams related URLs
    path('teams/', views.teams, name='teams'),
    path('teams/create/', views.team_create, name='team_create'),
    path('teams/<int:id>/', views.team_detail, name='team_detail'),
    
    # Placeholder URLs
    path('dashboard/', views.dummy_view, name='dashboard'),
    path('organisation/', include('skyapp.organization.urls')),
    path('messages/', views.dummy_view, name='messages'),
    path('schedule/', include('skyapp.schedule.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('reports/', include('skyapp.reports.urls')),


]
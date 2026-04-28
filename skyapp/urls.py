
from django.contrib import admin
from django.urls import path
from skyapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 
    path('teams/', views.teams, name='teams'),
    
    # Placeholder URLs to ensure teams.html can render without NoReverseMatch errors
    path('dashboard/', views.dummy_view, name='dashboard'),
    path('organisation/', views.dummy_view, name='organisation'),
    path('messages/', views.dummy_view, name='messages'),
    path('schedule/', views.dummy_view, name='schedule'),
    path('teams/create/', views.dummy_view, name='team_create'),
    path('teams/<int:id>/', views.dummy_view, name='team_detail'),
]

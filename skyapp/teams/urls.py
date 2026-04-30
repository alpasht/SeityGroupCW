from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login'), name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Teams related URLs
    path('teams/', views.teams, name='teams'),
    path('teams/create/', views.team_create, name='team_create'),
    path('teams/<int:id>/', views.team_detail, name='team_detail'),
    path('organization/', include('skyapp.organization.urls')),
    path('messages/', include('skyapp.messages_app.urls'), name='messages'),
    path('schedule/', include('skyapp.schedule.urls')),
    
    # Auth URLs
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('accounts/', include('django.contrib.auth.urls')), # Fallback for password change, etc.
    
    path('reports/', include('skyapp.reports.urls')),
    path('admin/', admin.site.urls),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

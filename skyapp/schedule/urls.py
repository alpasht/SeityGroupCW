from django.urls import path
from . import views

urlpatterns = [
    path('', views.meeting_list, name='schedule'),
    path('create/', views.meeting_create, name='meeting_create'),
    path('<int:pk>/edit/', views.meeting_update, name='meeting_update'),
    path('<int:pk>/delete/', views.meeting_delete, name='meeting_delete'),
    path('weekly/', views.weekly_view, name='weekly_view'),
    path('monthly/', views.monthly_view, name='monthly_view'),
    path('upcoming/', views.upcoming_meetings, name='upcoming_meetings'),
]

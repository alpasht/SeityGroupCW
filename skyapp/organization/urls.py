# Author: Mohammed Yousuf Moghal
# Student ID: w2073928
# Module: Organisation Module
# File: urls.py


from django.urls import path
from . import views

# Application page routes
urlpatterns = [
    path('', views.organization_home, name='organisation'),
    path('departments/', views.department_list, name='department_list'),
    path('departments/<int:department_id>/', views.department_detail, name='department_detail'),
    path('dependencies/', views.dependency_list, name='dependency_list'),
    path('team-types/', views.team_type_list, name='team_type_list'),
    path('teams/<int:team_id>/', views.team_detail, name='org_team_detail'),
]
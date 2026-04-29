# Author: Mohammed Yousuf Moghal
# Student ID: w2073928
# Module: Organisation Module
# File: views.py

from django.shortcuts import render, get_object_or_404
from .models import Department, Team, Dependency, TeamType


# Main organization map page
def organization_home(request):
    query = request.GET.get('q', '').strip()

    departments = Department.objects.all()
    teams = Team.objects.all()
    dependencies = Dependency.objects.all()

    # Filter results using search query
    if query:
        teams = teams.filter(name__icontains=query) | teams.filter(manager__icontains=query)

    departments = Department.objects.filter(
        id__in=teams.values_list('department_id', flat=True)
    ) | Department.objects.filter(name__icontains=query)

    context = {
        'departments': departments,
        'teams': teams,
        'dependencies': dependencies,
        'query': query,
    }

    return render(request, 'organization/home.html', context)

# Displays all departments in the organization
def department_list(request):
    query = request.GET.get('q')

    departments = Department.objects.all()

    if query:
        departments = departments.filter(name__icontains=query)

    return render(request, 'organization/department_list.html', {
        'departments': departments,
        'query': query,
    })

# Displays the selected apartments details
def department_detail(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    teams = Team.objects.filter(department=department)

    dependencies = Dependency.objects.filter(
        from_team__in=teams
    ) | Dependency.objects.filter(
        to_team__in=teams
    )

    return render(request, 'organization/department_detail.html', {
        'department': department,
        'teams': teams,
        'dependencies': dependencies,
    })

# Displays all team dependencies and relationships
def dependency_list(request):
    dependencies = Dependency.objects.select_related('from_team', 'to_team').all()

    return render(request, 'organization/dependency_list.html', {
        'dependencies': dependencies,
    })

# Displays all the team categories
def team_type_list(request):
    team_types = TeamType.objects.all()
    teams = Team.objects.all()

    return render(request, 'organization/team_type_list.html', {
        'team_types': team_types,
        'teams': teams,
    })

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)

    upstream = Dependency.objects.filter(to_team=team)
    downstream = Dependency.objects.filter(from_team=team)

    return render(request, 'organization/team_detail.html', {
        'team': team,
        'upstream': upstream,
        'downstream': downstream,
    })
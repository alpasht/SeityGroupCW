from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World")

def teams(request):
    return render(request, 'TEAMSPAGE/teams.html', {'teams': []})

def dummy_view(request, **kwargs):
    return HttpResponse("This page is not yet implemented.")

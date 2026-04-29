from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('skyapp.teams.urls')),
    path('reports/', include('skyapp.reports.urls')),
]
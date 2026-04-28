from django.contrib import admin
from .models import Team

#Registers the teamwithin django admin

admin.site.register(Team)
admin.site.register(Report)



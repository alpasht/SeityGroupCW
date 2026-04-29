# Author: Mohammed Yousuf Moghal
# Student ID: w2073928
# Module: Organisation Module
# File: admin.py



# Register models for admin management
from django.contrib import admin
from .models import Department, TeamType, Team, Dependency

admin.site.register(Department)
admin.site.register(TeamType)
admin.site.register(Team)
admin.site.register(Dependency)

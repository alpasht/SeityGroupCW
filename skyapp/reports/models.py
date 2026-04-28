from django.db import models

#Represents a yeam, storing info such as team name and the manager.

class Team(models.Model):
    team_name = models.CharField(max_length=100)
    manager = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.team_name
    #String representation that is used within the admin panel.
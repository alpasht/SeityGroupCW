# Author: Mohammed Yousuf Moghal
# Student ID: w2073928
# Module: Organisation Module
# File: models.py


from django.db import models

# Stores department information.
class Department(models.Model):
    name = models.CharField(max_length=100)
    leader = models.CharField(max_length=100)
    specialisation = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Stores info on reusable team categories. 
class TeamType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Stores the teams records linked to departments.
class Team(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    team_type = models.ForeignKey(TeamType, on_delete=models.SET_NULL, null=True)
    manager = models.CharField(max_length=100)
    purpose = models.TextField()
    contact_email = models.EmailField()
    slack_channel = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

# Stores relationships between the teams (upstream/downstream).
class Dependency(models.Model):
    DEPENDENCY_TYPES = [
        ('upstream', 'Upstream'),
        ('downstream', 'Downstream'),
    ]

    from_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='dependencies_from')
    to_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='dependencies_to')
    dependency_type = models.CharField(max_length=20, choices=DEPENDENCY_TYPES)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Dependencies"

    def __str__(self):
        return f"{self.from_team} -> {self.to_team}"

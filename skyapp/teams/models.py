from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    manager_email = models.EmailField()
    skills = models.CharField(max_length=255, help_text="Comma separated skills", blank=True, null=True)
    
    # New Fields
    purpose = models.CharField(max_length=255, blank=True, null=True, help_text="Brief mission statement or purpose of the team.")
    description = models.TextField(blank=True, null=True, help_text="Detailed responsibilities.")
    members = models.ManyToManyField(User, related_name='teams', blank=True)
    upstream = models.ManyToManyField('self', symmetrical=False, related_name='downstream', blank=True, help_text="Teams this team depends on.")
    code_repos = models.JSONField(default=list, blank=True, help_text="List of repository names.")

    @property
    def members_count(self):
        return self.members.count()

    @property
    def upstream_count(self):
        return self.upstream.count()

    @property
    def downstream_count(self):
        return self.downstream.count()

    def get_skills_list(self):
        if self.skills:
            return [s.strip() for s in self.skills.split(',') if s.strip()]
        return []

    def __str__(self):
        return self.name

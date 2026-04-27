from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    manager_email = models.EmailField()
    members_count = models.IntegerField(default=0)
    skills = models.CharField(max_length=255, help_text="Comma separated skills", blank=True, null=True)
    upstream_count = models.IntegerField(default=0)
    downstream_count = models.IntegerField(default=0)

    def get_skills_list(self):
        if self.skills:
            return [s.strip() for s in self.skills.split(',')]
        return []

    def __str__(self):
        return self.name

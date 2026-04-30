from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, help_text="Short bio or preferred contact method")

    def __str__(self):
        return f'{self.user.username} Profile'

# Automatically create/save Profile when User is created/saved
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

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

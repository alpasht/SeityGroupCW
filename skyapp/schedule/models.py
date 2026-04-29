from django.db import models
from django.contrib.auth.models import User
# from teams.models import Team

class Meeting(models.Model):

    PLATFORM_CHOICES = [
        ('teams', 'Microsoft Teams'),
        ('zoom', 'Zoom'),
        ('slack', 'Slack'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField(null=True, blank=True)

    platform = models.CharField(
        max_length=20,
        choices=PLATFORM_CHOICES,
        default='teams'
    )

    team = models.IntegerField()   # TEMPORARY placeholder
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.start_datetime.strftime('%Y-%m-%d %H:%M')})"


from django.shortcuts import render
from django.http import HttpResponse

# MOCK TEAM CLASS 
class MockTeam:
    def __init__(self, id, name, department, manager, email, size, skills, upstream, downstream):
        self.id = id
        self.name = name
        self.department = department
        self.manager = manager
        self.manager_email = email
        self.members_count = size
        self.skills = skills
        self.upstream_count = upstream
        self.downstream_count = downstream

    def get_skills_list(self):
        return [s.strip() for s in self.skills.split(',') if s.strip()]


# VIEWS 
def home(request):
    return HttpResponse("Hello World - Sky Engineering Portal")


def teams(request):
    """Teams List Page"""
    mock_teams = [
        MockTeam(1, "Platform Engineering", "Platform", "Sarah Chen", "sarah.chen@sky.uk", 
                 12, "Kubernetes, AWS, Terraform, Go", 5, 8),
        MockTeam(2, "Content Delivery", "Content", "Marcus Thorne", "marcus.thorne@sky.uk", 
                 8, "CDN, Varnish, Nginx, Python", 3, 12),
        MockTeam(3, "Streaming Services", "Streaming", "Elena Rodriguez", "elena.rodriguez@sky.uk", 
                 15, "Video Transcoding, HLS, DASH, Rust", 7, 4),
    ]
    return render(request, 'teams/teams.html', {'teams': mock_teams})


def team_detail(request, id):
    """Team Detail Page (for the 'Details' button)"""
    # Mock data for now
    mock_teams = {
        1: MockTeam(1, "Platform Engineering", "Platform", "Sarah Chen", "sarah.chen@sky.uk", 
                    12, "Kubernetes, AWS, Terraform, Go", 5, 8),
        2: MockTeam(2, "Content Delivery", "Content", "Marcus Thorne", "marcus.thorne@sky.uk", 
                    8, "CDN, Varnish, Nginx, Python", 3, 12),
        3: MockTeam(3, "Streaming Services", "Streaming", "Elena Rodriguez", "elena.rodriguez@sky.uk", 
                    15, "Video Transcoding, HLS, DASH, Rust", 7, 4),
    }
    
    team = mock_teams.get(id)
    if not team:
        return HttpResponse("Team not found", status=404)
    
    return render(request, 'teams/team_detail.html', {'team': team})


def dummy_view(request, **kwargs):
    """Placeholder for pages not implemented yet"""
    return HttpResponse("This page is not yet implemented.")


def team_create(request):
    """Placeholder for Create Team page"""
    return HttpResponse("Create New Team page - Coming soon!")
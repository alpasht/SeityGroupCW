from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World")

class MockTeam:
    def __init__(self, id, name, department, manager, email, size, skills, upstream, downstream, members=None, upstream_list=None, downstream_list=None, repositories=None):
        self.id = id
        self.name = name
        self.department = department
        self.manager = manager
        self.manager_email = email
        self.members_count = size
        self.skills = skills
        self.upstream_count = upstream
        self.downstream_count = downstream
        self.members = members or []
        self.upstream_list = upstream_list or []
        self.downstream_list = downstream_list or []
        self.repositories = repositories or []
    
    def get_skills_list(self):
        if isinstance(self.skills, list):
            return self.skills
        return [s.strip() for s in self.skills.split(',')]

def get_mock_teams():
    return [
        MockTeam(1, "Platform Engineering", "Platform", "Sarah Chen", "sarah.chen@sky.uk", 12, 
                 "Kubernetes, AWS, Terraform, Go", 5, 8,
                 members=["Alex Rivera (Lead)", "Sam Smith", "Jordan Lee", "Casey Wright"],
                 upstream_list=["Core Network", "Auth Service"],
                 downstream_list=["Content Delivery", "User API", "Analytics"],
                 repositories=["sky-platform-k8s", "terraform-provider-sky"]),
        MockTeam(2, "Content Delivery", "Content", "Marcus Thorne", "marcus.thorne@sky.uk", 8, 
                 "CDN, Varnish, Nginx, Python", 3, 12,
                 members=["Marcus Thorne (Lead)", "Taylor Swift", "Chris Evans"],
                 upstream_list=["Platform Engineering", "Video Ingest"],
                 downstream_list=["Streaming Services", "Player SDK"],
                 repositories=["sky-cdn-config", "varnish-vcl-master"]),
        MockTeam(3, "Streaming Services", "Streaming", "Elena Rodriguez", "elena.rodriguez@sky.uk", 15, 
                 "Video Transcoding, HLS, DASH, Rust", 7, 4,
                 members=["Elena Rodriguez (Lead)", "Tom Holland", "Zendaya"],
                 upstream_list=["Content Delivery", "Metadata API"],
                 downstream_list=["Mobile App", "Web Player", "Smart TV App"],
                 repositories=["sky-transcoder-rust", "streaming-manifest-gen"])
    ]

def teams(request):
    return render(request, 'TEAMSPAGE/teams.html', {'teams': get_mock_teams()})

def team_detail(request, id):
    teams_list = get_mock_teams()
    team = next((t for t in teams_list if t.id == id), None)
    if not team:
        return HttpResponse("Team not found", status=404)
    return render(request, 'TEAMSPAGE/team_detail.html', {'team': team})

def dummy_view(request, **kwargs):
    return HttpResponse("This page is not yet implemented.")

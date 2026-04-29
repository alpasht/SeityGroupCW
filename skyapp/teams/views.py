from django.shortcuts import render
from django.http import HttpResponse


# ===================== IMPROVED MOCK TEAM CLASS =====================
class MockTeam:
    def __init__(self, id, name, department, manager, email, size, skills,
                 upstream_count=0, downstream_count=0,
                 members=None, upstream_list=None, downstream_list=None,
                 repositories=None):
        
        self.id = id
        self.name = name
        self.department = department
        self.manager = manager
        self.manager_email = email
        self.members_count = size
        self.skills = skills
        self.upstream_count = upstream_count
        self.downstream_count = downstream_count
        
        # Optional fields
        self.members = members or []
        self.upstream_list = upstream_list or []
        self.downstream_list = downstream_list or []
        self.repositories = repositories or []

    def get_skills_list(self):
        if isinstance(self.skills, list):
            return self.skills
        return [s.strip() for s in self.skills.split(',') if s.strip()]


def get_mock_teams():
    return [
        MockTeam(
            id=1,
            name="Platform Engineering",
            department="Platform",
            manager="Sarah Chen",
            email="sarah.chen@sky.uk",
            size=12,
            skills="Kubernetes, AWS, Terraform, Go",
            upstream_count=5,
            downstream_count=8,
            upstream_list=["User API", "Database Team"],
            downstream_list=["Content Delivery", "Streaming Services"],
            repositories=["sky-platform-k8s", "terraform-provider-sky"]
        ),
        MockTeam(
            id=2,
            name="Content Delivery",
            department="Content",
            manager="Marcus Thorne",
            email="marcus.thorne@sky.uk",
            size=8,
            skills="CDN, Varnish, Nginx, Python",
            upstream_count=3,
            downstream_count=12,
            upstream_list=["Platform Engineering"],
            downstream_list=["Streaming Services", "Mobile Apps"],
            repositories=["sky-cdn-core", "varnish-config"]
        ),
        MockTeam(
            id=3,
            name="Streaming Services",
            department="Streaming",
            manager="Elena Rodriguez",
            email="elena.rodriguez@sky.uk",
            size=15,
            skills="Video Transcoding, HLS, DASH, Rust",
            upstream_count=7,
            downstream_count=4,
            upstream_list=["Content Delivery", "Platform Engineering"],
            downstream_list=["Analytics Team"],
            repositories=["sky-streaming-core", "hls-pipeline"]
        ),
    ]


# ===================== VIEWS =====================
def home(request):
    return HttpResponse("Hello World - Sky Engineering Portal")


def teams(request):
    #Teams List Page
    query = request.GET.get('q')
    mock_teams = get_mock_teams()
    
    if query:
        query = query.lower()
        mock_teams = [
            t for t in mock_teams 
            if query in t.name.lower() or 
               query in t.department.lower() or 
               query in t.manager.lower()
        ]
        
    return render(request, 'teams/teams.html', {
        'teams': mock_teams,
        'query': query
    })


def team_detail(request, id):
    #Team Detail Page
    mock_teams = get_mock_teams()
    team = next((t for t in mock_teams if t.id == id), None)
    
    if not team:
        return HttpResponse("Team not found", status=404)
    
    return render(request, 'teams/team_detail.html', {'team': team})


def team_create(request):
    #Create New Team Page
    return HttpResponse("Create New Team page - Coming soon!")


def dummy_view(request, **kwargs):
    #Placeholder for other pages
    return HttpResponse("This page is not yet implemented.")
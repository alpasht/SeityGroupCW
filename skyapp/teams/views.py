from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm

# ===================== AUTHENTICATION VIEWS =====================

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('dashboard')

class CustomLogoutView(LogoutView):
    next_page = 'login'

class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('dashboard')
    
    def form_valid(self, form):
        # Save the user and log them in automatically
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
        
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)

@login_required
def profile_edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile_edit')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        
    return render(request, 'registration/profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

# ===================== IMPROVED MOCK TEAM CLASS =====================
class MockTeam:
    def __init__(self, id, name, department, manager, email, size, skills,
                 purpose="", description="",
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
        self.purpose = purpose
        self.description = description
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
            manager="Olivia Carter",
            email="olivia.carter@sky.uk",
            size=5,
            skills="AWS, GCP, Terraform, Kubernetes",
            purpose="Provide reliable, scalable infrastructure for all Sky engineering teams.",
            description="Building and maintaining Sky's core platform infrastructure.",
            upstream_count=5,
            downstream_count=8,
            members=["Sarah Chen", "James Patel", "Emma Thompson", "Michael Rodriguez"],
            upstream_list=["Identity Platform", "Database Services"],
            downstream_list=["Content Delivery", "API Gateway"],
            repositories=["sky-platform-k8s", "terraform-provider-sky"]
        ),
        MockTeam(
            id=2,
            name="Cloud Hosting",
            department="Cloud",
            manager="Elijah Parker",
            email="elijah.parker@sky.uk",
            size=4,
            skills="AWS Lambda, API Gateway, Microservices, GraphQL, Node.js, Go",
            purpose="Manage and scale cloud compute and hosting environments.",
            description="Providing serverless and containerized hosting solutions.",
            upstream_count=3,
            downstream_count=12,
            members=["Daniel Kim", "Sophie Turner", "Lucas Grey"],
            upstream_list=["Platform Engineering"],
            downstream_list=["Mobile Apps", "Web Frontend"],
            repositories=["sky-cloud-hosting", "serverless-configs"]
        ),
        MockTeam(
            id=3,
            name="API Development",
            department="Backend",
            manager="Henry Ward",
            email="henry.ward@sky.uk",
            size=5,
            skills="OAuth, JWT, Postman, OpenAPI, Swagger, REST, gRPC",
            purpose="Design and implement core internal and external APIs.",
            description="Building secure and high-performance API endpoints.",
            upstream_count=7,
            downstream_count=4,
            members=["Oliver Smith", "Mia Johnson", "Jack Brown", "Amelia Davis"],
            upstream_list=["Cloud Hosting", "Database Services"],
            downstream_list=["Mobile Apps", "Partner Integrations"],
            repositories=["sky-core-api", "grpc-definitions"]
        ),
    ]


# ===================== VIEWS =====================
def dashboard(request):
    # Dashboard Overview Page
    mock_teams = get_mock_teams()
    
    total_teams = len(mock_teams)
    total_members = sum(t.members_count for t in mock_teams)
    
    # Extract all unique repos
    all_repos = set()
    for t in mock_teams:
        for repo in t.repositories:
            all_repos.add(repo)
    total_repos = len(all_repos)
    
    return render(request, 'dashboard.html', {
        'total_teams': total_teams,
        'total_members': total_members,
        'total_repos': total_repos,
        'recent_teams': mock_teams[:5]
    })


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
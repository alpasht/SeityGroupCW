from django.urls import path
from . import views

#URL configs for reports, which maps them to the view functions.

urlpatterns = [
    # Reports dashboard
    path('', views.reports_home, name='reports_home'),
    # Pdf export endpoint
    path('pdf/', views.export_pdf, name='export_pdf'),
    # Excel export endpoint
    path('excel/', views.export_excel, name='export_excel'),
]
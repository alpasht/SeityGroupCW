from django.shortcuts import render
from .models import Team
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from openpyxl import Workbook

# Used to retrieve data from db and display it in the reports template!
def reports_home(request):
    total_teams = Team.objects.count() # This is used to get the total number of teams.
    teams_with_manager = Team.objects.exclude(manager__isnull=True).exclude(manager="")
    #Teams that have a manager, excludes null oe empty values.
    teams_without_managers = Team.objects.filter(manager__isnull=True) | Team.objects.filter(manager="")
    #Teams that dont have a manager, includes null or empty values.

    #Preparation of data to template
    context = {
        "total_teams": total_teams,
        "teams_with_manager": teams_with_manager,
        "teams_without_managers": teams_without_managers,
        "all_teams": Team.objects.all(),
    }
    #Rendering the template with the data
    return render(request, "reports/reports_home.html", context)


#Generates a pdf which contains all teams and their managers, uses reportlab library to dynamically create the pdf.
def export_pdf(request):
    #CreAtes http response with pdf type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    
    p = canvas.Canvas(response) #Create pdf canvas

    teams = Team.objects.all() #Retrieve all teams

    y = 800 #Start position for the text within the pdf.
    p.drawString(100, y, "Teams Report") # The title of the report

    #Loops through the teams to add to the pdf.
    for team in teams:
        y -= 20
        manager = team.manager if team.manager else "No manager"
        p.drawString(100, y, f"{team.team_name} - {manager}")

    p.showPage()
    p.save()

    return response

def export_excel(request): #Generates excel report which has the team names and managers.
    #Uses openpyxl to create ss dynamically.
    wb = Workbook() #Creates a new workbook and sheet.
    ws = wb.active
    ws.title = "Teams Report"

    # Headers
    ws.append(["Team Name", "Manager"])

    teams = Team.objects.all()

    for team in teams: #Adds team data to spreadsheet.
        manager = team.manager if team.manager else "No manager"
        ws.append([team.team_name, manager])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=teams_report.xlsx'

    wb.save(response)

    return response
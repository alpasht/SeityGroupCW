from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Meeting
from .forms import MeetingForm
from datetime import datetime, timedelta, date
from django.utils import timezone
import calendar

# LIST MEETINGS
@login_required
def meeting_list(request):
    meetings = Meeting.objects.filter(created_by=request.user).order_by('start_datetime')
    return render(request, 'schedule/meeting_list.html', {'meetings': meetings})

# CREATE MEETING
@login_required
def meeting_create(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.created_by = request.user
            meeting.save()
            return redirect('schedule')   # UPDATED
    else:
        form = MeetingForm()
    return render(request, 'schedule/meeting_form.html', {'form': form})

# UPDATE MEETING
@login_required
def meeting_update(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk)
    if request.method == 'POST':
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect('schedule')   # UPDATED
    else:
        form = MeetingForm(instance=meeting)
    return render(request, 'schedule/meeting_form.html', {'form': form})

# DELETE MEETING
@login_required
def meeting_delete(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk)
    if request.method == 'POST':
        meeting.delete()
        return redirect('schedule')   # UPDATED
    return render(request, 'schedule/meeting_confirm_delete.html', {'meeting': meeting})

# WEEKLY VIEW
@login_required
def weekly_view(request):
    date_str = request.GET.get("week")
    if date_str:
        current_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    else:
        current_date = datetime.today().date()

    start_of_week = current_date - timedelta(days=current_date.weekday())
    days = [start_of_week + timedelta(days=i) for i in range(7)]

    # Convert dictionary keys to strings so templates can match them
    meetings_by_day = {}
    for day in days:
        meetings_by_day[str(day)] = Meeting.objects.filter(
            start_datetime__date=day,
            created_by=request.user
        ).order_by("start_datetime")

    previous_week = start_of_week - timedelta(days=7)
    next_week = start_of_week + timedelta(days=7)

    context = {
        "days": days,
        "meetings_by_day": meetings_by_day,
        "previous_week": previous_week,
        "next_week": next_week,
        "current_week": start_of_week,
    }

    return render(request, "schedule/weekly_view.html", context)

# MONTHLY VIEW
@login_required
def monthly_view(request):
    year = request.GET.get("year")
    month = request.GET.get("month")

    if year and month:
        year = int(year)
        month = int(month)
        current_date = date(year, month, 1)
    else:
        current_date = date.today().replace(day=1)

    cal = calendar.Calendar(firstweekday=0)
    month_days = cal.monthdatescalendar(current_date.year, current_date.month)

    meetings = Meeting.objects.filter(
        start_datetime__year=current_date.year,
        start_datetime__month=current_date.month,
        created_by=request.user
    )

    # Convert dictionary keys to strings
    meetings_by_day = {}
    for m in meetings:
        day = str(m.start_datetime.date())
        if day not in meetings_by_day:
            meetings_by_day[day] = []
        meetings_by_day[day].append(m)

    prev_month = (current_date.replace(day=1) - timedelta(days=1)).replace(day=1)
    next_month = (current_date.replace(day=28) + timedelta(days=4)).replace(day=1)

    context = {
        "month_days": month_days,
        "current_date": current_date,
        "meetings_by_day": meetings_by_day,
        "prev_month": prev_month,
        "next_month": next_month,
    }

    return render(request, "schedule/monthly_view.html", context)

# UPCOMING MEETINGS
@login_required
def upcoming_meetings(request):
    now = timezone.now()

    meetings = Meeting.objects.filter(
        created_by=request.user,
        start_datetime__gte=now
    ).order_by('start_datetime')[:5]

    return render(request, 'schedule/upcoming_meetings.html', {
        'meetings': meetings
    })

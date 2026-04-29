from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Message


def new_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user

            if 'send' in request.POST:
                message.status = 'sent'
                message.save()
                return redirect('sent_messages')

            elif 'draft' in request.POST:
                message.status = 'draft'
                message.save()
                return redirect('drafts')

    else:
        form = MessageForm()

    return render(request, 'messages_app/new_message.html', {'form': form})


def inbox(request):
    messages = Message.objects.filter(
        recipient=request.user,
        status='sent'
    ).order_by('-time_created')

    return render(request, 'messages_app/inbox.html', {'messages': messages})


def sent_messages(request):
    messages = Message.objects.filter(
        sender=request.user,
        status='sent'
    ).order_by('-time_created')

    return render(request, 'messages_app/sent.html', {'messages': messages})


def drafts(request):
    messages = Message.objects.filter(
        sender=request.user,
        status='draft'
    ).order_by('-time_updated')

    return render(request, 'messages_app/drafts.html', {'messages': messages})
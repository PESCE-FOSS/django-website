from datetime import date
from django.shortcuts import render
from .models import Event
from django.utils import timezone  # Import the timezone module


# def home(request):
#     return render(request, 'event/home.html')
def home(request):
    # Fetch events with a date in the future and order them by the event date
    upcoming_events = Event.objects.filter(date__gte=timezone.now()).order_by('date')  
    
    # Pass the events to the template
    return render(request, 'event/home.html', {'upcoming_events': upcoming_events})
def event(request):
    today = date.today()  # Get today's date

    # Fetch upcoming events (date >= today)
    upcoming_events = Event.objects.filter(date__gte=today).order_by('date')

    # Fetch past events (date < today)
    past_events = Event.objects.filter(date__lt=today).order_by('-date')

    context = {
        'upcoming_events': upcoming_events,
        'past_events': past_events,
    }

    return render(request, 'event/event.html', context)

def contact_us(request):
    return render(request, 'event/contact_us.html')

def vision(request):
    return render(request, 'event/vision.html')



from django.shortcuts import render
from .models import Ourteams,Ourwork


def ourteams(request):
    ourteams = Ourteams.objects.all()
    return render(request,'knowmore/ourteams.html',{'ourteams': ourteams})

def ourwork(request):
    ourwork = Ourwork.objects.all()
    return render(request,'knowmore/ourwork.html',{'ourwork': ourwork})


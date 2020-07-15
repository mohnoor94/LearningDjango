from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting


# Create your views here.
# A view is a Django Component that handles a request for a web page


def welcome(request):
    return render(request, 'website/welcome.html',
                  {
                      'number_of_meetings': Meeting.objects.count(),
                      'meetings': Meeting.objects.all(),
                  })


def time(request):
    return HttpResponse(f'This page was served at {datetime.now()}')


def about(request):
    return HttpResponse("I'm 'Mohammad Noor', your favourite Software Engineer!")

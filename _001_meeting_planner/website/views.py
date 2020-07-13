from datetime import datetime

from django.http import HttpResponse


# Create your views here.
# A view is a Django Component that handles a request for a web page
def welcome(request):
    return HttpResponse('Welcome to Meeting Planner!')


def time(request):
    return HttpResponse(f'This page was served at {datetime.now()}')


def about(request):
    return HttpResponse("I'm 'Mohammad Noor', your favourite Software Engineer!")



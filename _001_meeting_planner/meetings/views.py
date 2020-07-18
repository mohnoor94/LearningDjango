from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

from meetings.models import Meeting, Room


def detail(request, id):
    # meeting = Meeting.objects.get(pk=id)  # error page if id does not exist
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'meetings/detail.html', {
        'meeting': meeting,
    })


def rooms(request):
    return render(request, 'meetings/rooms.html', {
        'rooms': Room.objects.all(),
    })


MeetingForm = modelform_factory(Meeting, exclude=[])  # Generate a MeetingForm class


def create(request):
    if request.method == 'POST':
        # form has been submitted, process data
        form = MeetingForm(request.POST)  # create a new MeetingForm from the data that the user submitted!
        if form.is_valid():
            form.save()  # save to the DB
            return redirect('home')  # redirects to 'welcome' page url

    else:
        # request = 'GET'
        # Show the form so the user can fill and submit it!
        form = MeetingForm()

    return render(request, 'meetings/create.html', {
        'form': form
    })

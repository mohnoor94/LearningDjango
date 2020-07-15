from django.shortcuts import render, get_object_or_404

from meetings.models import Meeting


def detail(request, id):
    # meeting = Meeting.objects.get(pk=id)  # error page if id does not exist
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'meetings/detail.html', {'meeting': meeting})

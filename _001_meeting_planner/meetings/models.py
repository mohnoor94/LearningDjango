from datetime import time

from django.db import models


# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    floor = models.IntegerField()

    def __str__(self):
        return f'{self.name}: room {self.number} on floor {self.floor}'


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=30)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} on {self.date}, {self.start_time} for {self.duration // 60} hour(s) and {self.duration % 60} minutes'

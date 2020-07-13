from django.contrib import admin

from .models import Meeting, Room

# Register your models here.

admin.site.register(Meeting)  # Register meeting model so that it show up in the Admin Interface!
admin.site.register(Room)

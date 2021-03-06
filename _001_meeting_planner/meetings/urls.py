from django.urls import path

from meetings import views

urlpatterns = [
    path('<int:id>', views.detail, name='detail'),
    path('rooms', views.rooms, name='rooms'),
    path('create', views.create, name='create'),
]

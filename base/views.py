from django.shortcuts import render
from .models import CatRoom

# Create your views here.


def home(request):
    catRooms = CatRoom.objects.all()
    context = {
        'catRooms': catRooms
    }
    return render(request, 'base/home.html', context)


def catRoom(request, pk):
    catRoom = CatRoom.objects.get(id=pk)
    context = {
        'catRoom': catRoom
    }
    return render(request, 'base/catRoom.html', context)

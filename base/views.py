from django.shortcuts import render

# Create your views here.

catRooms = [
    {'id': 1, 'name': 'Nevertheless she PURRsisted!'},
    {'id': 2, 'name': 'Will Code for Catnips 🌿'},
    {'id': 3, 'name': 'Javascript Li(n)tter!'},
]


def home(request):
    context = {
        'catRooms':catRooms
    }
    return render(request, 'base/home.html',context)


def catRoom(request):
    return render(request, 'base/catRoom.html')

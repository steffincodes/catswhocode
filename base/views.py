from django.shortcuts import render, redirect
from django.db.models import Q
from .models import CatRoom, Topic
from .forms import CatRoomForm

# Create your views here.


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    catRooms = CatRoom.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    topics = Topic.objects.all()
    catRooms_count = catRooms.count()
    context = {
        'catRooms': catRooms,
        'topics': topics,
        'catRooms_count':catRooms_count
    }
    return render(request, 'base/home.html', context)


def catRoom(request, pk):
    catRoom = CatRoom.objects.get(id=pk)
    context = {
        'catRoom': catRoom
    }
    return render(request, 'base/catRoom.html', context)


def createCatRoom(request):
    form = CatRoomForm()
    if request.method == 'POST':
        form = CatRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/catRoom_form.html', context)


def updateCatRoom(request, pk):
    catRoom = CatRoom.objects.get(id=pk)
    form = CatRoomForm(instance=catRoom)
    if request.method == 'POST':
        form = CatRoomForm(request.POST, instance=catRoom)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/catRoom_form.html', context)


def deleteCatRoom(request, pk):
    catRoom = CatRoom.objects.get(id=pk)
    context = {'obj': catRoom}
    if request.method == 'POST':
        catRoom.delete()
        return redirect('home')

    return render(request, 'base/delete.html', context)

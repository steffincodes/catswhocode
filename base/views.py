from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib.auth.models import User
from .models import CatRoom, Topic
from .forms import CatRoomForm

# Create your views here.


def loginRegister(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User not found')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Authetication Failed')

    context = {}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


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
        'catRooms_count': catRooms_count
    }
    return render(request, 'base/home.html', context)


def catRoom(request, pk):
    catRoom = CatRoom.objects.get(id=pk)
    context = {
        'catRoom': catRoom
    }
    return render(request, 'base/cat_room.html', context)


@login_required(login_url='/login')
def createCatRoom(request):
    form = CatRoomForm()
    if request.method == 'POST':
        form = CatRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/cat_room_form.html', context)


@login_required(login_url='/login')
def updateCatRoom(request, pk):
    catRoom = CatRoom.objects.get(id=pk)
    form = CatRoomForm(instance=catRoom)
    if request.user != catRoom.hostCat:
        return HttpResponse('You are not allowed here...')
    if request.method == 'POST':
        form = CatRoomForm(request.POST, instance=catRoom)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/cat_room_form.html', context)


@login_required(login_url='/login')
def deleteCatRoom(request, pk):
    catRoom = CatRoom.objects.get(id=pk)
    context = {'obj': catRoom}
    if request.user != catRoom.hostCat:
        return HttpResponse('You are not allowed here...')

    if request.method == 'POST':
        catRoom.delete()
        return redirect('home')

    return render(request, 'base/delete.html', context)

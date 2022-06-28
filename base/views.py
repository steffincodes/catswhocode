from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib.auth.models import User
from .models import CatRoom, Topic, Meow
from .forms import CatRoomForm
# Create your views here.


def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')  # .lower()
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
    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Unable to register...')
    context = {'form': form}
    return render(request, 'base/login_register.html', context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    cat_rooms = CatRoom.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    topics = Topic.objects.all()
    cat_rooms_count = cat_rooms.count()
    context = {
        'cat_rooms': cat_rooms,
        'topics': topics,
        'cat_rooms_count': cat_rooms_count
    }
    return render(request, 'base/home.html', context)


def cat_room(request, pk):
    cat_room = CatRoom.objects.get(id=pk)
    meows = cat_room.meow_set.all().order_by('-created')
    participants = cat_room.participants.all()
    if request.method == "POST":
        meows = Meow.objects.create(
            cat=request.user,
            catRoom=cat_room,
            body=request.POST.get('body')
        )
        cat_room.participants.add(request.user)
        return redirect('cat_room', pk=cat_room.id)

    context = {
        'cat_room': cat_room,
        'meows': meows,
        'participants': participants
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
    cat_room = CatRoom.objects.get(id=pk)
    form = CatRoomForm(instance=cat_room)
    if request.user != cat_room.hostCat:
        return HttpResponse('You are not allowed here...')
    if request.method == 'POST':
        form = CatRoomForm(request.POST, instance=cat_room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/cat_room_form.html', context)


@login_required(login_url='/login')
def deleteCatRoom(request, pk):
    cat_room = CatRoom.objects.get(id=pk)
    context = {'obj': cat_room}
    if request.user != cat_room.hostCat:
        return HttpResponse('You are not allowed here...')
    if request.method == 'POST':
        cat_room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', context)

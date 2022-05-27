from django.shortcuts import render
# from django.http import HttpResponse 

# Create your views here.

def home(request):
    # return HttpResponse('Home Page')
    return render(request, 'home.html')

def catRoom(request):
    # return HttpResponse('Cat Room')
    return render(request, 'catRoom.html')
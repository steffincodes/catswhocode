from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cat-room/<str:pk>', views.catRoom, name='catRoom'),
    path('create-cat-room/', views.createCatRoom, name='createCatRoom'),
]

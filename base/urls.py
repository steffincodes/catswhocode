from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('catRoom/<str:pk>', views.catRoom,name='catRoom'),
]

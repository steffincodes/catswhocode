from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('', views.home, name='home'),
    path('cat-room/<str:pk>', views.cat_room, name='cat_room'),

    path('create-cat-room/', views.createCatRoom, name='createCatRoom'),
    path('update-cat-room/<str:pk>', views.updateCatRoom, name='updateCatRoom'),
    path('delete-cat-room/<str:pk>', views.deleteCatRoom, name='deleteCatRoom'),
]

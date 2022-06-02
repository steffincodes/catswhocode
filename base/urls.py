from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginRegister, name = 'login'),
    path('logout/',views.logoutUser, name = 'logout'),

    path('', views.home, name='home'),
    path('cat-room/<str:pk>', views.catRoom, name='catRoom'),

    path('create-cat-room/', views.createCatRoom, name='createCatRoom'),
    path('update-cat-room/<str:pk>', views.updateCatRoom, name='updateCatRoom'),
    path('delete-cat-room/<str:pk>', views.deleteCatRoom, name='deleteCatRoom'),
]

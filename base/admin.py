from django.contrib import admin

# Register your models here.

from .models import Topic,CatRoom,Meow

admin.site.register(Topic)
admin.site.register(CatRoom)
admin.site.register(Meow)
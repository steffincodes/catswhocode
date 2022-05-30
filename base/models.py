from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class CatRoom(models.Model):
    hostCat = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(
        null=True, blank=True)  # can be blank in db & UI
    updated = models.DateTimeField(auto_now=True)  # every saved change
    created = models.DateTimeField(auto_now_add=True)  # first saved change

    def __str__(self):
        return str(self.name)


class Meow(models.Model):
    cat = models.ForeignKey(User, on_delete=models.CASCADE)
    catRoom = models.ForeignKey(CatRoom, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)  # every saved change
    created = models.DateTimeField(auto_now_add=True)  # first saved change

    def __str__(self):
        return str(self.body[0:50])

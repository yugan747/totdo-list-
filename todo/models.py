from django.db import models
from django.contrib.auth.models import User 

class Profile(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)

class Todolist(models.Model):
    Descriptions = models.CharField(max_length=400)
    Remainder = models.DateTimeField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
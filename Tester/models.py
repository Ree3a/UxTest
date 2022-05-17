from tkinter import CASCADE
import black
from click import password_option
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UxTester(models.Model):
    user=models.OneToOneField(User, on_delete=CASCADE,null=True,blank=True)
    id=models.AutoField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=100,blank=True,null=False)
    email=models.CharField(max_length=100,blank=True,null=False)
    phone=models.CharField(max_length=10,blank=True,null=False)
    password=models.CharField(max_length=30,blank=True,null=False)

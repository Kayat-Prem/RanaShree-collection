import uuid
from django.contrib import admin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from users.models import CustomUser
from django.contrib.auth.decorators import login_required


def Adminn(request):
    return render(request, 'adminn.html')

def edit_profile(request):
    return render(request, 'edit_profile.html')

def logout(request):
    return render(request, 'index.html')
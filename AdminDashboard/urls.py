from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth

urlpatterns = [
    path("adminn/", views.Adminn, name ='adminn'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('logout/', views.logout, name='logout'),
] 

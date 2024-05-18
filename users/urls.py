"""Ranashreecollection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from .import views
from django.contrib.auth import views as auth

urlpatterns = [

    path("", views.LandingPage, name='index'),
    path("about/", views.AboutUs, name='about'),
    path("blog/", views.Blog, name='blog'),
    path("contact/", views.Contact, name='contact'),
    path("refund/", views.Refund, name='refund'),
    path("PrivacyPolicy/", views.PrivacyPolicy, name='privacy'),
    path("faq/", views.faq, name='faq'),
    path("login/", views.Login, name ='login'),
    path("signup/", views.Signup, name='signup'),
    path('verify/<str:token>/',views.VerifyEmail,name='verify_email'),
    path('forgot-password/',views.ForgotPassword,name='forgot_password'),
    path('reset-password/<str:token>/',views.ResetPassword,name='reset_password'),
    path('inputcontact/',views.inputcontact, name='inputcontact'),
    path('auth-receiver', views.auth_receiver, name='auth_receiver'),
    path("testimonial/", views.Testimonial, name='testimonial'),


    path("products/", views.products, name='products'),
    path("individualProducts/<int:id>", views.individualProducts, name='individualProducts'),
    path("addCart/", views.addCart, name='addCart'),
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('delete-from-cart/<int:item_id>/', views.delete_from_cart, name='delete_from_cart'),
    path("placeOrder/<int:id>", views.placeOrder, name='placeOrder'),
    path('place_order/',views.place_order, name='placeOrders'),
    path("transaction/<int:id>", views.Transaction, name='transaction'),
    # path('place_order/',views.place_order, name='placeOrders'),

    path('api/verify_payment/', views.verify_payment, name='verify_payment'),
] 

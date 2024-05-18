from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from .import views
from django.contrib.auth import views as auth

urlpatterns = [
    path("adminn/", views.Adminn, name ='adminn'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('logout/', views.logout, name='logout'),
    path('allproducts/', views.Allproducts, name='allproducts'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('allusers/', views.Allusers, name='allusers'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('allorders/', views.Allorders, name='allorders'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('transaction/', views.Transaction, name='transaction'),
    path('delete_transaction/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
    path('settings/', views.Settings, name='settings'),
    path('adminCart/', views.AdminCart, name='adminCart'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
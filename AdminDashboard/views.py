import uuid
from django.contrib import admin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from users.models import CustomUser
from django.contrib.auth.decorators import login_required
from .models import productsModel
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.contrib.auth.models import User


def Adminn(request):
    return render(request, 'adminn.html')

def edit_profile(request):
    return render(request, 'edit_profile.html')

def logout(request):
    return render(request, 'index.html')


def Allproducts(request):
    if request.method == 'POST':
        name = request.POST.get('Sari_Name')
        description = request.POST.get('Description')
        ldescription = request.POST.get('LDescription')
        size = request.POST.get('Size')
        image = request.FILES.get('Image')
        price = request.POST.get('Price')
        
        if name and description and ldescription and size and image and price:
            productsModel.objects.create(Sari_Name=name, Description=description, LDescription=ldescription, Size=size, Image=image, Price=price)
            messages.success(request, "Successfully Added!")
            return redirect('allproducts')  
        else:
            messages.error(request, "All fields are required.")

    products = productsModel.objects.all()
    
    return render(request, 'allproducts.html', {'products': products})


def edit_product(request, product_id):
    product = productsModel.objects.get(id=product_id)
    
    if request.method == 'POST':
        product.Sari_Name = request.POST.get('Sari_Name')
        product.Description = request.POST.get('Description')
        product.ldescription = request.POST.get('LDescription')
        product.size = request.POST.get('Size')
        product.Price = request.POST.get('Price')
        
        # Check if a new image file was uploaded
        image = request.FILES.get('Image')
        if image:
            product.Image = image
        product.save()
        messages.success(request, "Product updated successfully!")
        return redirect('allproducts')
    products = productsModel.objects.all()
    
    return render(request, 'edit_product.html', {'product': product, 'products': products})


def delete_product(request, product_id):
    if request.method == 'POST':
        try:
            product = productsModel.objects.get(id=product_id)
            product.delete()
            return JsonResponse({'success': True})
        except productsModel.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Product does not exist'}, status=404)
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)


def Allusers(request):
    all_users = CustomUser.objects.all()
    return render(request, 'allusers.html', {'users': all_users})

def delete_user(request, user_id):
    if request.method == 'POST':
        try:
            user = CustomUser.objects.get(id=user_id)
            if user.is_superuser:
                return JsonResponse({'success': False, 'error': 'Superuser cannot be deleted'})
            else:
                user.delete()
                return JsonResponse({'success': True})
        except CustomUser.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'User does not exist'}, status=404)
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)
    

def Allorders(request):
    return render(request, 'allorders.html')


def Settings(request):
    return render(request, 'settings.html')
import uuid
from django.contrib import admin
from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .utils import *
import re
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from google.oauth2 import id_token
from google.auth.transport import requests
from django.contrib.auth.decorators import login_required
from AdminDashboard.models import productsModel

def LandingPage(request):
        products = productsModel.objects.all()
        return render(request, 'users/index.html', {'products': products})

# @login_required(login_url='/login/')
# def LandingPage(request):
#         if request.username.is_authenticated:
#             products = CustomUser.objects.filter(username=request.username)
#         else:
#             products = []
#         return render(request, 'users/index.html', {'products': products})


# @login_required(login_url='/login/') 
# def UserPage(request):
#     products = productsModel.objects.all()
#     return render(request, 'users/user.html', {'products': products})



def AboutUs(request):
        return render(request, "users/about.html")

def Blog(request):
    return render(request, "users/blog.html")

def Contact(request):
    return render(request, "users/contact.html")

def Refund(request):
    return render(request, "users/refund.html")

def PrivacyPolicy(request):
    return render(request, "users/PrivacyPolicy.html")

def faq(request):
    return render(request, "users/faq.html")

def Testimonial(request):
    return render(request, "users/testimonial.html")

def products(request):
    products = productsModel.objects.all()
    return render(request, "users/products.html", {'products': products})

def individualProducts(request, id):
    product = productsModel.objects.get(id=id)
    return render(request, "users/individualProduct.html", {'product': product})

def individualProducts(request, id):
    try:
        product = productsModel.objects.get(id=id)
        print("Sari Product found:", product) 
    except productsModel.DoesNotExist:
        print("Sari Product not found")  
    return render(request, "users/individualProduct.html", {'product': product})

def placeOrder(request, id):
    product = productsModel.objects.get(id=id)
    return render(request, "users/placeOrder.html", {'product': product})

def placeOrder(request, id):
    try:
        products = get_object_or_404(productsModel, id=id)
     
        return render(request, "users/placeOrder.html", {'product': products})
    except productsModel.DoesNotExist:
        messages.error(request, "Product not found.")  
        return redirect('products')  




def addCart(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
    else:
        cart_items = []
    return render(request, "users/addCart.html", {'cart_items': cart_items})


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from AdminDashboard.models import Cart
from decimal import Decimal

        # ### Add to cart Items. ###
@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        user = request.user if request.user.is_authenticated else None
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        size = request.POST.get('size')
        image = request.POST.get('image')
        quantity = int(request.POST.get('quantity', 1)) 

        price_str = request.POST.get('price')
        price = Decimal(price_str.replace('Rs. ', '').replace(',', '')) 
        
        # Check if the product already exists in the cart
        existing_item = Cart.objects.filter(
            user=user,
            product_name=product_name,
            description=description,
            size=size
        ).first()

        if existing_item:
            # If the product already exists, update the quantity instead of creating a new entry
            existing_item.quantity += quantity
            existing_item.save()
        else:
            # If the product does not exist, create a new entry in the cart
            cart_item = Cart.objects.create(
                user=user,
                product_name=product_name,
                description=description,
                price=price,
                size=size,
                image=image,
                quantity=quantity
            )
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Only POST requests are allowed.'})


    # ### Detete sigle item from the cart ###
from django.shortcuts import get_object_or_404  
def delete_from_cart(request, item_id):
    item = get_object_or_404(Cart, id=item_id)
    item.delete()
    return redirect('addCart')




# #### SIGN UP ###
def Signup(request):
    context = {
                'username': '',
                'fullname': '',
                'email': '',
                'contact': '',
                'pass1': '',
                'pass2': '',
            }
    if request.method == 'POST':
        username= request.POST['username'] # accesed from the name in the form
        fullname= request.POST['fullname']
        email= request.POST['email']
        contact= request.POST['contact'] 
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']

        context = {
                'username': username,
                'fullname': fullname,
                'email': email,
                'contact': contact,
                'pass1': pass1,
                'pass2': pass2,
            }
        status=False
        if CustomUser.objects.filter(username=username):
            status=True
            messages.error(request, "Username is already in use. Please choose a different username.")
      
        if CustomUser.objects.filter(email=email):
            status=True
            messages.error(request, "Email address is already in use. Please use a different email.")
        
        if len(username) > 15:
            status=True
            messages.error(request, "The username cannot be longer than 15 characters.")

        if pass1!=pass2:
             status=True
             messages.error(request, "The passwords don't match.")

        alphanumeric_pattern = re.compile(r'^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{8,}$')

        # Check if username contains only alphanumeric characters
        if not alphanumeric_pattern.match(username):
            status = True
            
            messages.error(request, "The username must be alphanumeric and contain atleast 8 characters.")

       

        # Check if password contains only alphanumeric characters
        if not alphanumeric_pattern.match(pass1):
            status = True
            messages.error(request, "The password must be alphanumeric and contain atleast 8 characters.")

        if CustomUser.objects.filter(contact_number=contact):    
            status=True
            messages.error(request, "The contact number is already in use. Please choose a different contact number.")
           
        if len(str(contact)) !=10:
            status=True
            print("hello")
            messages.error(request, "The contact number should be exactly 10 digits" )

        if status:
          return render(request, 'users/signup.html',context)
           
        email_token = str(uuid.uuid4())
        my_user=CustomUser.objects.create_user(username,email,pass1)
        my_user.full_name=fullname
        my_user.contact_number=contact
        my_user.email_token = email_token
        my_user.save()
        send_email_token(email,email_token)
        messages.success(request, "Your account was successfully created. Please check your email for verification.")
        return redirect('login')
        

    return render(request, 'users/signup.html',context)


def Login(request):
    context = {'username': ''}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass1'] 

        context = {'username': username}
        user = authenticate(username=username, password=password)
        if user is not None and user.is_verified:  # Check if user is verified
            login(request, user)
            if user.is_superuser:  # Check if user is an admin
                messages.success(request, "Admin login successful!")
                return redirect('adminn')  # Redirect to admin page
            else:
                fullname = user.full_name
                messages.success(request, "Successfully logged in!")
                return redirect("index")
        elif user is not None and not user.is_verified:
            messages.error(request, "Your email is not verified yet. Please check your email for verification.")
            
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'users/login.html', context)


def VerifyEmail(request, token):
    try:
        user = CustomUser.objects.get(email_token=token)
        user.is_verified = True
        user.save()
        messages.success(request, "Your email has been verified. You can now log in.")
    except CustomUser.DoesNotExist:
        messages.error(request, "Invalid verification token.")

    return redirect('login')

def ForgotPassword(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        try:
            user = CustomUser.objects.get(username=username)
            email= user.email

            # Generate a unique token for password reset
            password_token = str(uuid.uuid4())
            user.password_reset_token = password_token
            user.save()
            send_password_token(email,password_token)

        
            messages.success(request, "Password reset link has been sent to your email.")
            return redirect('forgot_password')

        except CustomUser.DoesNotExist:
            messages.error(request, "User not found.")
            return redirect('forgot_password')

    return render(request, 'users/forgot-password.html')


def ResetPassword(request, token):
   
    try:
        user = CustomUser.objects.get(password_reset_token=token)
        
        if request.method == 'POST':
            new_password = request.POST.get('new-password')
            confirm_password = request.POST.get('confirm-password')
           

            if new_password != confirm_password:
                messages.error(request, "Passwords don't match")
                return redirect(f'/reset-password/{token}/')
            
            alphanumeric_pattern = re.compile(r'^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{8,}$')

            if not alphanumeric_pattern.match(new_password):
                messages.error(request, "The password must be alphanumeric and contain atleast 8 characters.")
                return redirect(f'/reset-password/{token}/')
            
         
            user.set_password(new_password)
            user.save()
            messages.success(request,"Your password was reset successfully!")
            return redirect('login')

    except CustomUser.DoesNotExist:
        messages.error(request, "Invalid password reset token")
        return redirect('forgot_password')

    return render(request, 'users/reset-password.html')



@csrf_exempt
def auth_receiver(request):
    """
    Google calls this URL after the user has signed in with their Google account.
    """
    token = request.POST['credential']

    try:
        user_data = id_token.verify_oauth2_token(
            token, requests.Request(), '803641603998-mtkrdl2sq8797su0okkm6v96epn5eo65.apps.googleusercontent.com'
        )
        print(user_data)
        
        
    except ValueError:
        return HttpResponse(status=403)

    
    try:
        user = CustomUser.objects.get(email=user_data['email'])
        login(request, user)

        return redirect('index')
    except CustomUser.DoesNotExist:
        
        user = CustomUser.objects.create_user(
            username=user_data['email'],  
            email=user_data['email'],
            full_name=user_data.get('name', ''),
            is_verified=True
        )

    # Log in the user
    login(request, user)
    return redirect('inputcontact')


def inputcontact(request):
    if request.method == 'POST':
        contact = request.POST.get('contact_number')
        status=False
        if CustomUser.objects.filter(contact_number=contact):    
          status=True
          messages.error(request, "The contact number is already in use. Please choose a different contact number.")
        
        if len(str(contact)) !=10:
            status=True
     
            messages.error(request, "The contact number should be exactly 10 digits" )

        if status:
            return render(request, 'users/inputcontact.html')

        request.user.contact_number = contact
        request.user.save()
        messages.success(request, "login successful")
        return redirect('index')  
    
    return render(request, 'users/inputcontact.html')


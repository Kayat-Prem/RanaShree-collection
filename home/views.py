from django.http import HttpResponse
from django.shortcuts import render, redirect

# def AboutUs(request):
#     return HttpResponse("Ranashree Collection")


def LandingPage(request):
    data={
        'Title': 'Ranashree Collection'
    }
    return render(request, 'index.html', data)  # data jun chai HTML page maa dekhauna chahancha....

def AboutUs(request):
    return render(request, "about.html")

def Blog(request):
    return render(request, "blog.html")

def Contact(request):
    return render(request, "contact.html")
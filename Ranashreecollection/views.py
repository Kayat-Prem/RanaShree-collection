from django.http import HttpResponse

def AboutUs(request):
    return HttpResponse("Khima Collection")

def aboutus(request, write):
    return HttpResponse(write)
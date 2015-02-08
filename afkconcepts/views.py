from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    #return HttpResponse(home/home.htm)
    return render(request, 'home/home.htm')

def services(request):
    return render(request, 'home/services.htm')

def contact(request):
    return render(request, 'home/contact.htm')
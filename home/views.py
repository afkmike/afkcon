__author__ = 'Mark'
from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse


def index(request):
    #return HttpResponse("Testaroonie")
    #return render(request, reverse('index'))
    return render(request, 'home/home.htm')


def contact(request):
    return render(request, 'home/contact.htm')


def services(request):
    return render(request, 'home/services.htm')


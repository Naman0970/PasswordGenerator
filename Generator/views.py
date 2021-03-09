from django.http import HttpResponse
from django.shortcuts import render
import random


# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def passgenerator(request):
    password = ''
    characters = list('abcdefghjklmnopqrstuvwxyz')
    length=int(request.GET.get('length'))

    if(request.GET.get('uppercase')):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if(request.GET.get('numbers')):
        characters.extend('0123456789')
    if(request.GET.get('specials')):
        characters.extend('!@#$%^&')

    for x in range(length):
        password += random.choice(characters)

    return render(request, 'generator/passgenerator.html' , {'passgenerator' : password})

def about(request):
    return render(request,'generator/about.html')



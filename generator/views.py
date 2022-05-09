from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
#home function which is being called in the url patterns is created 

def home(request):
    return render(request,'generator/home.html')

def password(request):
    characters=list('abcdefgijklmnopqrstuvwxyz')
    length=int(request.GET.get('length'))

    uppercase=request.GET.get('Uppercase')
    Numericals=request.GET.get('Numericals')
    Special_Characters=request.GET.get('Special_Characters')

    if uppercase:
        characters.extend('ABCDEFGIJKLMNOPQRSTUVWXYZ')
    if Numericals:
        characters.extend('1234567890')
    if Special_Characters:
        characters.extend('~!@#$%^&*()_-')        

    thepassword=" "

    for x in range(length):
        thepassword+=random.choice(characters)
    return render(request,'generator/password.html',{'password':thepassword})    
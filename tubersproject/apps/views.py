from django.http import request
from django.shortcuts import render
import pytube 
from pytube import *

# Create your views here.


def Home(request):
    
    return render(request, 'index.html')


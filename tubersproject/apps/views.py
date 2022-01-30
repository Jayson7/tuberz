from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages
# from django.urls import resolve

import pytube 
from pytube import *
# Create your views here.



def Home(request):
   
    
    return render(request, 'index.html' ) 



def Small(request):
    # current_url = resolve(request.path_info).url_name
    # checking whether request.method is post or not
    
    context = {}
    try:
        if request.method == 'POST':
        
            
            # getting link from frontend
            link = request.POST['link']
            video = YouTube(link)
            # title
            video_title = video.title
            # thumbnail
            
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            
            # smallest resolution
            
            smallest_resolution = video.streams.get_lowest_resolution()
            smallest_resolution.download()
            
            # downloads video
            # stream.download()
    
            # returning HTML page
            
            return render(request, 'small.html')

    except:
        redirect ('/')
    
    return render(request, 'small.html')

def Large(request):
    # current_url = resolve(request.path_info).url_name
    # checking whether request.method is post or not
    context = {}
    try:
        if request.method == 'POST':
       
            # getting link from frontend
            link = request.POST['link']
            video = YouTube(link)
            # title
            video_title = video.title
        
        
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # highest resolution
            highest_resolution = video.streams.get_highest_resolution()
            highest_resolution.download()
        
    
            # returning HTML page
            messages.success(request, 'Your file is currently downloading', extra_tags='alert')
            return render(request, 'large.html')

    except:
        messages.warning(request, 'Please correct the error below.')
        redirect ('/')
    return render(request, 'large.html')

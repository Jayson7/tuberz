from django.http import request
from django.shortcuts import render, redirect
from django.urls import resolve

import pytube 
from pytube import *
# Create your views here.



def Home(request):
    # checking whether request.method is post or not
    current_url = resolve(request.path_info).url_name
    if request.method == 'POST':
        context = {}
        # getting link from frontend
        link = request.POST['link']
        video = YouTube(link)
        # title
        video_title = video.title
        # thumbnail
        thumbnail_urls = video.thumbnail_url
        print(current_url)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        context['video_title', 'thumbnail_urls'] = video_title, thumbnail_urls
    
        return render(request, 'index.html', context ) 
    
    return render(request, 'index.html' ) 

def Small(request):
    current_url = resolve(request.path_info).url_name
    # checking whether request.method is post or not
    context = {}
    if request.method == 'POST':
        print(current_url)
        
        # getting link from frontend
        link = request.POST['link']
        video = YouTube(link)
        # title
        video_title = video.title
        # thumbnail
        
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
        # smallest resolution
        
        smallest_resolution = video.streams.get_lowest_resolution()
        
          
        # downloads video
        # stream.download()
 
        # returning HTML page
        return render(request, 'index.html')
    
    return render(request, 'index.html')

def Large(request):
    current_url = resolve(request.path_info).url_name
    # checking whether request.method is post or not
    context = {}
    if request.method == 'POST':
       
        # getting link from frontend
        link = request.POST['link']
        video = YouTube(link)
        # title
        video_title = video.title
       
      
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # highest resolution
        highest_resolution = video.streams.get_highest_resolution()
        highest_resolution_download = highest_resolution.download()
       
        print(highest_resolution)  
    
 
        # returning HTML page
      
    
    return render(request, 'index.html')

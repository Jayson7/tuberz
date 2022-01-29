from django.http import request
from django.shortcuts import render, redirect
import pytube 
from pytube import *

# Create your views here.


def Home(request):
    # checking whether request.method is post or not
    context = {}
    if request.method == 'POST':
       
        # getting link from frontend
        link = request.POST['link']
        video = YouTube(link)
        # title
        video_title = video.title
        # thumbnail
        thumbnail_url = video.thumbnail.url
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # highest resolution
        highest_resolution = video.streams.get_highest_resolution()
        highest_resolution_download = highest_resolution.download()
        # setting video resolution
        stream = video.streams.get_lowest_resolution()
        print(stream)  
        # downloads video
        # stream.download()
 
        # returning HTML page
        return render(request, 'index.html')
    
    return render(request, 'index.html')

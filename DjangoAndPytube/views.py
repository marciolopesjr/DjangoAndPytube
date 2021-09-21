from django.shortcuts import render, redirect
from pytube import *
import pytube 

def youtube(request):

    if request.method == 'POST':

        link = request.POST['link']
        video = YouTube(link)

        stream = video.streams.get_lowest_resolution()
        stream.download()
        
        return render(request, 'templates/youtube.html')

    return render(request, 'templates/youtube.html')
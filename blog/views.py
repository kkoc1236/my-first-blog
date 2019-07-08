from django.shortcuts import render
from .models import Post
from django.utils import timezone
import re

def gps(request):
    if request.method == 'POST':
        converted =  {'gpsinfo': gpsinfo}
        return render(converted, 'blog/post_list.html', {'gpsinfo;'})
    else:
        return render(request, 'blog/post_list.html', {})
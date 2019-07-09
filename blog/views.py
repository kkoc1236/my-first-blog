from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.http import HttpResponseRedirect
import re

def gps(request):
    if request.method == 'post':
        converted1 = 'Hello'
        return render(request, 'blog/post_list.html', {'converted1' : converted1})
    else:
        converted = 'World'
        return render(request, 'blog/post_list.html', {'convert' : converted})
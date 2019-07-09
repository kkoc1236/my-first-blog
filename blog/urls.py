from django.urls import path
from . import views
from django.shortcuts import render, get_object_or_404
urlpatterns = [
    path('', views.gps, name='gps'),
    path('blog/post_list.html', views.gps, name='gps'),

]
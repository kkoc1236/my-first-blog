from django.urls import path
from . import views
from django.shortcuts import render, get_object_or_404
urlpatterns = [
    path('', views.home),
    path('newpage/',  views.new_page,  name="my_function")
]
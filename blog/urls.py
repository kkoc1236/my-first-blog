from django.urls import path
from . import views

urlpatterns = [
    path('', views.gps, name='gps'),
]
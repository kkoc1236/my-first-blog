from django.urls import path
from . import views
from . import views_report
from . import views_sky_gps

from django.shortcuts import render, get_object_or_404
urlpatterns = [
    path('', views.home),
    path('newpage/',  views.new_page,  name="my_function"),
    path('report/', views_report.home),
    path('report/report',  views_report.report,  name="my_report"),
    path('sky_gps/', views_sky_gps.home),
    path('sky_gps/sky_gps',  views_sky_gps.sky_gps,  name="my_sky_gps"),
]
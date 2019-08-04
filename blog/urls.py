from django.urls import path
from . import views
from . import views_report
from . import views_sky_gps
from . import views_rcc
from . import views_rcc1
from . import views_rcc2

from django.shortcuts import render, get_object_or_404
urlpatterns = [
    path('', views.home),
    path('newpage/',  views.new_page,  name="my_function"),
    path('report/', views_report.home),
    path('report/report',  views_report.report,  name="my_report"),
    path('sky_gps/', views_sky_gps.home),
    path('sky_gps/sky_gps',  views_sky_gps.sky_gps,  name="my_sky_gps"),
    path('rcc/', views_rcc.home),
    path('rcc/rcc',  views_rcc.rcc,  name="my_rcc"),
    path('rcc1/', views_rcc1.home),
    path('rcc1/rcc1',  views_rcc1.rcc1,  name="my_rcc1"),
    path('rcc/rcc2', views_rcc2.home),
    path('rcc/rcc2/rcc2',  views_rcc2.rcc2,  name="my_rcc2"),
    path('rcc/comment1', views_rcc.comment1),
    path('rcc/comment2', views_rcc.comment2),


]
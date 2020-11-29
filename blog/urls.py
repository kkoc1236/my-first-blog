from django.urls import path
from django.conf.urls import url, handler404
from . import views
from . import views_report
from . import views_sky_gps
from . import views_rcc
from . import views_rcc1
from . import views_rcc2
from . import xml_file_extractor

from django.shortcuts import render, get_object_or_404

handler400 = "kkoc1236.views.error400"
handler404 = "kkoc1236.views.error404"
handler500 = "kkoc1236.views.wrong file"

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
    path('xml_file_extractor/', xml_file_extractor.home),
    path('xml_file_extractor/xml_file_extractor', xml_file_extractor.extracting, name="xml_file_extractor"),
    path('rcc/comment0', views_rcc.comment0), path('rcc/comment1', views_rcc.comment1), path('rcc/comment2', views_rcc.comment2), path('rcc/comment3', views_rcc.comment3), path('rcc/comment4', views_rcc.comment4), path('rcc/comment5', views_rcc.comment5), path('rcc/comment6', views_rcc.comment6), path('rcc/comment7', views_rcc.comment7), path('rcc/comment8', views_rcc.comment8), path('rcc/comment9', views_rcc.comment9), path('rcc/comment10', views_rcc.comment10), path('rcc/comment11', views_rcc.comment11), path('rcc/comment12', views_rcc.comment12),


]
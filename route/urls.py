"""gmap URL Configuration
"""
from django.conf.urls import url
from . import views

app_name = "route"

urlpatterns = [
    url(r'^usermap', views.usermap, name='usermap'),
    url(r'^getdestination', views.getdestination, name='getdestination'),
    url(r'^getallroutes', views.getallroutes, name='getallroutes'),
    url(r'^userroute', views.userroute, name='userroute'),
    url(r'^adddata', views.adddata, name='adddata'),
    url(r'^', views.index, name='index'),
]

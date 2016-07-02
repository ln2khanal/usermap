"""sujentask URL Configuration
"""
from django.conf.urls import url
from . import views

app_name = "route"

urlpatterns = [
    url(r'^usermap', views.usermap, name='usermap'),
    url(r'^', views.index, name='index'),
]

"""gmap URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^route/', include('route.urls'), name='routeindex'),
    url(r'^', views.index, name='index'),
]

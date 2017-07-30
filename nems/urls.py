"""nems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from nems.views import *

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^home/$', home, name='home'),
	url(r'^projects/$', projects, name='projects'),
	url(r'^publications/$', publications, name='publications'),
	url(r'^people/$', people, name='people'),
	url(r'^links/$', links, name='links'),
	url(r'^gallery/$', gallery, name='gallery'),
	url(r'^download/$', download, name='download'),
	url(r'^demo/$', demo, name='demo'),
]

# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns  = [
    url(r'^$',views.index,name='index'),
    url(r'^about.html$',views.about,name='about'),
    #url(r'^Trending.html$',views.trend,name='trend'),
]

#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^article/(?P<article_id>\d+)$', views.article_page, name='article_page'),
    url(r'^edit/(?P<article_id>\d+)$', views.edit_page, name="edit_page2"),
    url(r'^edit/action/$', views.edit_action, name="edit_action"),
    url(r'^$', views.index),
]
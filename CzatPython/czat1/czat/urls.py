# -*- coding: utf-8 -*-
# czat/urls.py

from django.urls import path
from . import views  # import widoków aplikacji

app_name = 'czat'  # przestrzeń nazw aplikacji
urlpatterns = [
    path('', views.index, name='index'),
    path('loguj/', views.loguj, name='loguj'),
    path('wyloguj/', views.wyloguj, name='wyloguj'),
    path('wiadomosci/', views.wiadomosci, name='wiadomosci'),
]

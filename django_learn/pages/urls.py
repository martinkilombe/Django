#pages/urls.py

from django.urls import path
from .views import homepageview

#Define urls patterns
urlpatterns = [
    path('',homepageview,name= 'home'),
]
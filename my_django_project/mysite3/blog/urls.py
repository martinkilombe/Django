#blog/urls.py
from django.urls import path
from . import views

#defining the URls patterns
urlpatterns = [
    path('',views.homepage,name='homepage'),
]
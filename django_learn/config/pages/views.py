#pages/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.
#Hompage view
class HomePageView(TemplateView):
    template_name = 'home.html'


#About Page view
class AboutPageView(TemplateView):
    template_name = 'about.html'
    
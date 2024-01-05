#blog/views.py
from django.shortcuts import render
from django.views.generic import ListView
from .models import blog

# Create your views here.
class HomepageView(ListView):
    model = blog
    template_name = 'home.html'
    context_object_name = 'all_posts_list' #Covers all the post lists
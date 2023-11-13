#blog/views.py
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'blog/Homepage.html')
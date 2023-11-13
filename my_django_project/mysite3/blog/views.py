#blog/views.py
from django.shortcuts import render
from .models import Comment
from django.http import HttpResponseRedirect


# Create your views here.
def homepage(request):
    comments = Comment.objects.all()
    return render(request,'blog/Homepage.html',{'comments':comments})


def add_comment(request):
    if request.method == 'POST':
        text = request.POST.get('comment_text')
        if text:
            Comment.objects.create(text=text)
    return HttpResponseRedirect('/')
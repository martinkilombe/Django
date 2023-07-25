from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
# Create your views here.
"""def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))"""
#shorter way -- render()
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request,question_id):
    return HttpResponse("You are looking at question %s" % question_id)

def results(request,question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id) 

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
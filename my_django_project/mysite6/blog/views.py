#blog/views
from django.shortcuts import render

# Create your views here.
#Revenue Analysis
def Revenue_Analysis(request):
    return render(request,'blog/Revenue_Analysis.html')

#Customer Behaviour
def Customer_Behaviour(request):
    return render(request,'blog/Customer_Behaviour.html')

#Account Analysis
def Account_Analysis(request):
    return render(request,'blog/Account_Analysis.html')
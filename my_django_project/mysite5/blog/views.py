#blog/views
from django.shortcuts import render

# Create your views here.
#Revenue Page
def revenue(request):
    return render(request,'blog/Revenue.html')

#Customer Analysis page
def Customer_Analysis(request):
    return render(request,'blog/Customer_Analysis.html')

#Customer Behaviour page
def Custmer_Behaviour(request):
    return render(request,'blog/Customer_Behaviour.html')


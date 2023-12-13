#blog/urls.py
from django.urls import path
from .views import Revenue_Analysis, Cusomer_Behaviour, Account_Analysis

urlpatterns = [
    path('revenue-analyis/', Revenue_Analysis, name='Revenue_Analysis'),
    path('customer-behaviour-analysis/',Cusomer_Behaviour,name = 'Customer_Behaviour'),
    path('account-analysis/',Account_Analysis,name='Account_Analysis'),
     #Add other URL paterns as needed
]

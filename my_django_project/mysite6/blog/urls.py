#blogs/urls.py

from django.urls import path
from . import views

#Create Urlpatterns
urlpatterns=[
    path('revenue-analysis/',views.Revenue_Analysis,name='Revenue_Analysis'),
    path('customer-behaviour-analysis/',views.Customer_Behaviour,name='Customer_Behaviour'),
    path('account-analysis',views.Account_Analysis,name='Account_Analysis'),
]
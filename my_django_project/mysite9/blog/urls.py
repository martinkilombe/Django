# blog/urls.py
from django.urls import path
from .views import Revenue_Analysis,Customer_Behaviour,Account_Analysis
urlpatterns = [
    path('revenue-analysis/', Revenue_Analysis, name='Revenue_Analysis'),
    path('customer-behaviour-analysis/',Customer_Behaviour,name='Customer_Behaviour'),
    path('account-analysis/',Account_Analysis,name='Account_Analysis'),
    # Add other URL patterns as needed
]

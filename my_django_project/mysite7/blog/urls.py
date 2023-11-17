# blog/urls.py
from django.urls import path
from .views import Revenue_Analysis,Customer_Behaviour
urlpatterns = [
    path('revenue-analysis/', Revenue_Analysis, name='Revenue_Analysis'),
    path('customer-behaviour-analysis/',Customer_Behaviour,name='Customer_Behaviour')
    # Add other URL patterns as needed
]

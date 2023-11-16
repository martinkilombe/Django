#blogs/urls.py

from django.urls import path
from . import views

urlpatterns= [
    path('revenue-analysis/',views.revenue,name='revenue'),
    path('customer-account-analysis/',views.Customer_Analysis,name='Customer_Analysis'),
    path('customer-behavior-analysis/',views.Customer_Behaviour,name='Customer_Behaviour'),
]

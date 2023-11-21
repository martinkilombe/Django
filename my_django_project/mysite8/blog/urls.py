#blogs/urls.py
from django.urls import path
from .views import Revenue_Analysis,Account_Analysis,Customer_Behaviour,Product_Analysis

urlpatterns=[
    path('revenue-analysis/',Revenue_Analysis,name='Revenue_Analysis'),
    path('customer-behaviur-analysis/',Customer_Behaviour,name='Customer_Behaviour'),
    path('account-analysis/',Account_Analysis,name='Account_Analysis'),
    path('product-analysis/',Product_Analysis,name='Product_Analysis'),

    #Add other URL patterns
]
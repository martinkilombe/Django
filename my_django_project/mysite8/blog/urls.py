#blogs/urls.py
from django.urls import path
from .views import Revenue_Analysis,Account_Analysis,Customer_Behaviour

urlpatterns=[
    path('revenue-analysis/',Revenue_Analysis,name='Revenue_Analysis'),
    path('customer-behaviur-analysis/',Customer_Behaviour,name='Customer_Behaviour'),
    path('account-analysis/',Account_Analysis,name='Account_Analysis'),

    #Add other URL patterns
]
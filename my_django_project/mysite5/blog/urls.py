#blogs/urls.py

from django.urls import path
from . import views

urlpatterns= [
    path('',views.revenue,name='revenue'),
    path('',views.Customer_Analysis,name='Customer_Analysis'),
    path('',views.Custmer_Behaviour,name='Custmer_Behaviour'),
]

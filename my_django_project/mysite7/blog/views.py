#blog/views.py
from django.shortcuts import render
import jwt
import time



# Create your views here.
#Revenue Analysis
def Revenue_Analysis(request):
    METABASE_SITE_URL = "http://localhost:3000"
    METABASE_SECRET_KEY = "b3dd70e957bd04a868d85e812ca5322c9e1ae09026dabc12e48211fe74e0056b"

    # Define the payload for the JWT token
    payload = {
        "resource": {"dashboard": 3},  # Adjust the dashboard ID as needed
        "params": {},
        "exp": round(time.time()) + (60 * 10)  # 10-minute expiration
    }

    # Generate the JWT token
    token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

    # Construct the iframe URL
    iframe_url = METABASE_SITE_URL + f"/embed/dashboard/{token}#bordered=true&titled=true"

    # Render a template with the iframe URL
    return render(request, 'blog/Revenue_Analysis.html', {'iframe_url': iframe_url})



#Customer Behaviour Analysis
def Customer_Behaviour(request):
    METABASE_SITE_URL = "http://localhost:3000"
    METABASE_SECRET_KEY = "b3dd70e957bd04a868d85e812ca5322c9e1ae09026dabc12e48211fe74e0056b"

    # Define the payload for the JWT token
    payload = {
        "resource": {"dashboard": 4},
        "params": {},
        "exp": round(time.time()) + (60 * 10)  # 10 minute expiration
    }

    # Generate the JWT token
    token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

    # Construct the iframe URL
    iframe_url = METABASE_SITE_URL + "/embed/dashboard/" + token + "#bordered=true&titled=true"

    # Render a template with the iframe URL
    return render(request, 'blog/Customer_Behaviour.html', {'iframe_url': iframe_url})

#Account Analysis
def Account_Analysis(request):
    METABASE_SITE_URL = "http://localhost:3000"
    METABASE_SECRET_KEY = "b3dd70e957bd04a868d85e812ca5322c9e1ae09026dabc12e48211fe74e0056b"

    # Define the payload for the JWT token
    payload = {
        "resource": {"dashboard": 2},
        "params": {},
        "exp": round(time.time()) + (60 * 10)  # 10-minute expiration
    }

    # Generate the JWT token
    token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

    # Construct the iframe URL
    iframe_url = METABASE_SITE_URL + "/embed/dashboard/" + token + "#bordered=true&titled=true"

    # Render a template with the iframe URL
    return render(request, 'blog/Account_Analysis.html', {'iframe_url': iframe_url})
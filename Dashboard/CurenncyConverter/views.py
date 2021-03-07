from django.shortcuts import render

import requests


# Create your views here.

def index(request, base: str):
    response = requests.get(f'https://api.exchangeratesapi.io/latest?base={base.upper()}')
    curenncy_data = response.json()
    return render(request, "currency.html", context=curenncy_data)

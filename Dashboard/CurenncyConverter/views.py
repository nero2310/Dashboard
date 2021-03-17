from django.shortcuts import render

import requests


# Create your views here.

def index(request, base: str):
    response = requests.get(f'https://api.exchangeratesapi.io/latest?base={base.upper()}')
    if response:
        currency_data = response.json()
        return render(request, "currency.html", context=currency_data)
    elif response.status_code == 400:
        error_data = {
            'Status_Code': response.status_code,
            'Message': 'Check if the currency selected is correct'
        }
        return render(request, "api-error.html", context=error_data)
    else:
        error_data = {
            'Status_Code': response.status_code,
            'Message': 'Unexpected error'
        }
        return render(request, "api-error.html", context=error_data)

from django.shortcuts import render

# Create your views here.

def index(request,base):
    return render(request, template_name="currency.html")
from django.shortcuts import render

# Create your views here.

from .models import Item

def index(request):
    return render(request, 'Home/index.html')
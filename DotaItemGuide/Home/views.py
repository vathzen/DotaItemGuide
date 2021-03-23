from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

from .models import Item

def index(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        q = Item.objects.filter(hint__icontains=query)
        return render(request, 'Home/index.html',{'items': q})
    else:
        return render(request, 'Home/index.html')
from django.shortcuts import render
from ecommapp.models import Product
# Create your views here.

def index(request):

    context={'ecommapp': Product.objects.all()}
    return render(request, 'home/index.html',context)
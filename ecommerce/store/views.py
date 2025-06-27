from django.shortcuts import render
from .models import *
# Create your views here.

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)

def cart(request):
    """
    Render the cart page.
    """
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    """
    Render the checkout page.
    """
    context = {}
    return render(request, 'store/checkout.html', context)  

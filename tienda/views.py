from django.shortcuts import render

# Create your views here.


def tienda(request):
     context = {}
     return render(request, 'tienda/tienda.html', context)

def cart(request):
     context = {}
     return render(request, 'tienda/cart.html', context)

def checkout(request):
      context = {}
      return render(request, 'tienda/checkout.html', context)

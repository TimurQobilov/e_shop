from django.shortcuts import render
from .models import Product, CategoryProduct

# Create your views here.
def home_page(request):
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'home.html', context)
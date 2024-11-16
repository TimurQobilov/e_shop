from django.shortcuts import render
from .models import Product, CategoryProduct

# Create your views here.
def home_page(request):
    products = Product.objects.all()
    categories = CategoryProduct.objects.all()

    context = {'products': products, 'categories' : categories}

    return render(request, 'home.html', context)


def category_page(request, pk):
    category = CategoryProduct.objects.get(id=pk)
    products = Product.objects.filter(product_category=category)

    context = {'products': products}

    return render(request, 'category.html', context)

def product_page(request, pk):
    product = Product.objects.get(id=pk)

    context = {'product': product}

    return  render(request, 'product.html', context)























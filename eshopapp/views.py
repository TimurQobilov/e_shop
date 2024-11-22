from django.shortcuts import render,redirect
from .models import Product, CategoryProduct, News



# Create your views here.


def home_page(request):
    try:
        if request.user.is_authenticated:
            products = Product.objects.all()
            categories = CategoryProduct.objects.all()

            context = {'products': products, 'categories' : categories}

            return render(request, 'index.html', context)
        return redirect('about')
    except:
        return redirect('about')


def category_page(request, pk):
    category = CategoryProduct.objects.get(id=pk)
    products = Product.objects.filter(product_category=category).all()

    context = {'products': products, "category" : category}

    return render(request, 'category_product.html', context)

def product_page(request, pk):
    product = Product.objects.get(id=pk)

    context = {'product': product}

    return  render(request, 'product.html', context)

def news_page(request):
    news = News.objects.all()
    context = {'news': news}

    return render(request, 'news.html', context)

def about(request):
    try:
        if request.user.is_authenticated:
            redirect("home_page")
        return render(request, 'about.html')
    except:
        return redirect('about')



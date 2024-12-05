import telebot
from django.shortcuts import render,redirect
from .models import Product, CategoryProduct, News, UserCart

bot = telebot.TeleBot("7870735481:AAGZtMthZdqGBFIDKVJAKRGxhhwYEpUgnfQ")


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

def aboutus(request):
    try:
        if request.user.is_authenticated:
            redirect("aboutus")
            return render(request, 'aboutus.html')
    except:
        return redirect('aboutus')

def add_product_to_cart(request, pk):
    if request.method == "POST":
        checker = Product.objects.get(id=pk)
        if checker.product_count >= int(request.POST.get('pr_count')):
            UserCart.objects.create(user_id = request.user.id, product=checker, product_count=int(request.POST.get
                                                                                                  ('pr_count')))
            print("SUCCESS")

            return  redirect('user_cart')
        else:
            print("ERROR")
            return redirect("home")

def user_cart(request):
    cart = UserCart.objects.filter(user_id=request.user.id).all()
    if request.method == "POST":
        main_text = 'У вас новый заказ'

        for i in cart:
            main_text += (f"\n Товар: {i.product.product_name}"
                          f"\n Кол-во: {i.product_count}"
                          f"\n ID-пользователя: {i.user_id}"
                          f"\n Цена: {i.product.product_cost}")
            bot.send_message(-4652600005, main_text)
            cart.delete()
            return redirect('home')

    else:
        return render(request, "user_cart.html", context={"cart": cart})

























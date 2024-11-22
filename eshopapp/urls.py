from django.urls import path
from . import views
from user.views import register_view

urlpatterns = [
    path('', views.home_page),
    path('category/<int:pk>', views.category_page),
    path('product/<int:pk>', views.product_page),
    path('news/', views.news_page),
    path('register/', register_view),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('about/', views.about_page, name='about'),
]
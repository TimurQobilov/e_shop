from django.db import models

# Create your models here.
class CategoryProduct(models.Model):
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    product_name = models.CharField(max_length=55)
    product_cost = models.FloatField()
    product_descr = models.TextField()
    product_image = models.FileField(upload_to="product_image")
    product_count = models.IntegerField(default=0)
    product_category = models.ForeignKey(CategoryProduct,
                                         on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class UserCart(models.Model):
    user_id = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id, self.product

    class Meta:
        verbose_name = "User Cart"
        verbose_name_plural = "User Carts"


class NewsCategory(models.Model):
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.category_name

class News(models.Model):
    news_name = models.CharField(max_length=100)
    news_desc = models.TextField()
    news_image = models.FileField(upload_to="news_image")
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_name

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"





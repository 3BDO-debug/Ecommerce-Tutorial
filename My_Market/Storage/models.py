from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=500, verbose_name="Category Name")
    category_description = models.TextField(verbose_name="Category Description")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural ="Categories"

    def __str__(self):
        return f"{self.category_name}"

class Product(models.Model):
    product_img = models.ImageField(verbose_name="Product Image")
    product_category = models.ForeignKey(Category, on_delete=CASCADE, verbose_name= "Product Category")
    product_name = models.CharField(max_length=500, verbose_name="Product Name")
    product_size = models.CharField(max_length=50 ,verbose_name="Product Size")
    product_price = models.IntegerField(verbose_name="Product Price")
    product_description = models.TextField(verbose_name="Product Description")
    newly_arrived = models.BooleanField(default=False)
    best_seller = models.BooleanField(default= False)
    most_wanted = models.BooleanField(default= False)



    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural ="Products"

    def __str__(self):
        return f"{self.product_name}"
    
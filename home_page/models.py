from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    user_id = models.CharField(max_length=30, primary_key=True)  
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)  
    password = models.CharField(max_length=128) 
    profile_image = models.ImageField(upload_to='profile_images/')  
    date_of_join = models.DateField(_("Date of Joining"), auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Stores(models.Model):
    store_id = models.CharField(max_length=30, primary_key=True)
    store_name = models.CharField(max_length=30, blank=False, null=True)  
    store_description = models.CharField(max_length=100)
    store_logo = models.ImageField(upload_to='store_logos/') 
    store_creation_date = models.DateField(_("Date of Creation"), auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='store' ,default=None)  # One-to-one relationship

class Products(models.Model):
    store = models.ForeignKey('Stores', on_delete=models.CASCADE)  # ForeignKey to Store model
    product_id = models.AutoField(primary_key=True)  
    product_name = models.CharField(max_length=255, blank=False, null=False)  
    description = models.CharField(max_length=500, blank=True, null=True) 
    price = models.FloatField()  
    category = models.CharField(max_length=100)  
    stock = models.IntegerField() 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')  # ForeignKey for the user


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)  # ? AutoField for review_id 
    rating = models.IntegerField()                   # todos: Integer for rating
    review_text = models.CharField(max_length=500)
    review_date = models.DateField(auto_now_add=True)  #! Auto set the date when the review is created
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='reviews')  # !Link reviews to products
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews') 
    def __str__(self):
        return f"Review by {self.user.name} on {self.product.product_name}"


class ShoppingCart(models.Model):  
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shopping_cart')
    products = models.ManyToManyField(Products, related_name='carts')  # A cart can have many products
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.name}"
    



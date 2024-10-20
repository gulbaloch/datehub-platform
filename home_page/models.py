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



class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=100)

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            'user', 
            'role'
            )  # Ensures a user can't have the same role multiple times


class Stores(models.Model):
    store_id = models.CharField(max_length=30, primary_key=True)
    store_name = models.CharField(max_length=30, blank=False, null=True)  
    store_description = models.CharField(max_length=100)
    store_logo = models.ImageField(upload_to='store_logos/') 
    store_creation_date = models.DateField(_("Date of Creation"), auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stores')
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='store' ,default=None)  # One-to-one relationship

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
    review_id = models.AutoField(primary_key=True)  
    rating = models.IntegerField()  # e.g., a rating out of 5
    review_text = models.TextField()  # The actual review text
    review_date = models.DateField(auto_now_add=True)  
    product = models.ForeignKey('Products', on_delete=models.CASCADE)  # Links review to a product
    user = models.ForeignKey('User', on_delete=models.CASCADE)  # Links review to the user who wrote it

    def __str__(self):
        return f"Review {self.review_id} by {self.user.name} for {self.product.product_name}"



class ShoppingCart(models.Model):  
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shopping_cart')
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.name}"

class CartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name='items')  # Link to shopping cart
    product = models.ForeignKey(Products, on_delete=models.CASCADE)  # Link to product
    quantity = models.IntegerField(default=1)  # Allows for multiple quantities of the same product

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name} in Cart {self.cart.cart_id}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.CharField(max_length=255)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    payment_method = models.BooleanField()  # True = card, False = other methods
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class Transaction(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField(auto_now_add=True)
    transaction_status = models.BooleanField()  # True = successful, False = failed
class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wishlist')
    date_created = models.DateField(auto_now_add=True)
class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name='wishlist_items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

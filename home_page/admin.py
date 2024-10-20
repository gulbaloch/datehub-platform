from django.contrib import admin
from .models import CartItem, Order, OrderItem, Payment, Products, Transaction, User, Stores ,Review,ShoppingCart, Wishlist, WishlistItem
admin.site.register(User)
admin.site.register(Stores)
admin.site.register(Products)
admin.site.register(Review)
admin.site.register(ShoppingCart)
admin.site.register(Payment)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Transaction)
admin.site.register(Wishlist)
admin.site.register(WishlistItem)


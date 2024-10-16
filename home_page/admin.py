from django.contrib import admin
from .models import Products, User, Stores ,Review,ShoppingCart
admin.site.register(User)
admin.site.register(Stores)
admin.site.register(Products)
admin.site.register(Review)
admin.site.register(ShoppingCart)



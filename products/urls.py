from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    path('', views.productsDetails, name='productsDetails'),  # Base /products URL
]

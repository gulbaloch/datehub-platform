from django.urls import path
from . import views

urlpatterns = [
    path('user_reg/', views.registration, name='user_reg'),
    path('login/', views.login, name='login'),
]

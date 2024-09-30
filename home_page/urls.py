from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('user_profile/', views.User_profile, name='user_profile'), 
]

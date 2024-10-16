from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('user_profile/', views.User_profile, name='user_profile'), 
    path('show_user/<str:user_id>/', views.User_show, name='userShow'),
]

from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home_page, name='home_page'),  # Base / URL
    path('user/<str:user_id>/', views.user, name='user'),  # URL for user page (with trailing slash)
]

from django.shortcuts import render ,get_object_or_404
from .models import User

def home_page(request):
    return render(request, 'index.html')  

def user(request, user_id):
    user = get_object_or_404(User, user_id=user_id)
    return render(request, 'users.html', {'user':user})




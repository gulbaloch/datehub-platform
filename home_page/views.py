from django.shortcuts import redirect, render, get_object_or_404
from .models import User
from .forms import User_forms


def User_profile(request):
    if request.method == "POST":
        form = User_forms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("successful")
    else:
        form = User_forms()

    return render(request, "users.html", {"form": form})


def home_page(request):
    return render(request, "index.html")


def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, "users.html", {"user": user})

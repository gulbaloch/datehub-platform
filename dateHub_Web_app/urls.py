from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home_page.urls")),
    path("accounts/", include("accounts.urls")),
    path("products/", include("products.urls")),
    path("about/", include("static_pages.urls")),
]

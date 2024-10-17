from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Import settings
from django.conf.urls.static import static  # Import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home_page.urls")),
    path("accounts/", include("accounts.urls")),
    path("products/", include("products.urls")),
    path("about/", include("static_pages.urls")),
    path("addtocart/", include("cart.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('verification/', include('verify_email.urls')),

    path("", include("base.urls")),
    path("messagebox/", include("messagebox.urls", namespace="messagebox")),
    
]
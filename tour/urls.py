from django.urls import include, path
from django.contrib import admin
from main import views

urlpatterns = [
    path("", views.home),
    path("admin/", admin.site.urls),
    path("main/", include("main.urls")),
    path("account/", include("custom_account.urls")),
]

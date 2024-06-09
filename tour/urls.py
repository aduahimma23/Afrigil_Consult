from django.urls import include, path
from django.contrib import admin
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home),
    path("admin/", admin.site.urls),
    path("main/", include("main.urls")),
    path("account/", include("custom_account.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from main import views
from custom_account.views import AdminLoginView, AdminLogoutView

urlpatterns = [
    path("", views.home),
    path("admin/", admin.site.urls),
    path("main/", include("main.urls")),
    path("account/", include("custom_account.urls")),
    path('admin/login/', AdminLoginView.as_view(), name='admin-login'),
    path('admin/logout/', AdminLogoutView.as_view(), name='admin-logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
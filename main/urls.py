from .views import *
from django.urls import path

app_name = "main"

urlpatterns = [
    path("home", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("service/", service, name="service"),
    path("passport/", passport, name="passport"),
    path("birthcert/", birthcert, name="birthcert"),
    path("bookflight/", bookflight, name="bookflight"),
    path("package/", package, name="package"),
    path("bookpackage/", bookpackage, name="bookpackage"),
    path("hotel_reserve/", hotel_reserve, name="hotel_reserve"),
    path("scholarship_link/", scholarship_link, name="scholar")
]
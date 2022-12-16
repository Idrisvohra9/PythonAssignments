from django.urls import path
from HaideriGreens import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="Store"),
    path("About", views.about, name="About Us"),
    path("Sign_up", views.signup, name="Sign up"),
    path("Products", views.products, name="Products"),
    path("Visit", views.visit, name="Visit Us"),
    path("basket", views.basket, name="basket"),
    path("Donate", views.donate, name="donate"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

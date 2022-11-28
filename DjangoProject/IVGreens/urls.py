from django.urls import path
from IVGreens import views


urlpatterns = [
    path("", views.index, name="Store"),
    path("About Us", views.about, name="About Us"),
    path("Login", views.login, name="Login"),
    path("Register", views.register, name="Register"),
    path("Products", views.products, name="Products"),
    path("Visit", views.visit, name="Visit Us"),
]

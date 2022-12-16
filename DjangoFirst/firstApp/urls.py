from django.urls import path
from firstApp import views

urlpatterns = [
    # If the path url matches the empty string send the request to the views.py's index function and name the path 'Home'
    path("index", views.index, name="index"),
    path("About", views.about, name="About"),
    # We can also name it similar name so even if a spelling mistake occurs it still goes to the about page
    path("about", views.about, name="About"),
    path("", views.index, name="Form"),
]

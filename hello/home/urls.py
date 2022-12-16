from django.contrib import admin
from django.urls import path
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path("",views.index,name='index'),
    path("login",views.test,name='test'),
    path("delete/<int:id>",views.delete,name='delete'),
    path("update/<int:id>",views.update,name='update'),
    path("update/updaterecord/<int:id>",views.updaterecord,name='updaterecord')
]

urlpatterns += staticfiles_urlpatterns()
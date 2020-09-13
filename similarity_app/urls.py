from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "similarity"

urlpatterns = [
    path("", views.index, name = "index"),
    path("title/", views.title, name = "title"),
    path("abstract/", views.abstract, name = "abstract"),  
    ]



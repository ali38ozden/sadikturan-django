from django.contrib import admin
from django.urls import path
from . import views
            # http://127.0.0.1:8000/            => index
            # http://127.0.0.1:8000/index       => index
            # http://127.0.0.1:8000/blogs       => blog
            # http://127.0.0.1:8000/blogs/3     => blog-details

urlpatterns = [
    path("", views.index),
    path("index", views.index),
    path("blogs", views.blogs),
    path("blogs/<int:number>", views.blogs_details), # buradaki id ve views.py deki id farklı bir isim yap öyle dene olunca
]

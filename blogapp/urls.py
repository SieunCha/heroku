from django.contrib import admin
from django.urls import path
from . import views #import blogapp.views랑 같은 의미

urlpatterns = [
    path('<int:blog_id>/', views.detail, name = "detail"),
    path('new/', views.new, name = "new"),
    path('create/', views.create, name = "create"),
    path('newblog/', views.blogpost, name="newblog"),
]
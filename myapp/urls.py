from django.contrib import admin
from django.urls import path
from myapp import views 


urlpatterns = [
    path("", views.index, name='index'),
    path("signup", views.handleSignup, name='handleSignup'),
    path("login", views.handleLogin, name='handleLogin'),
    path("logout", views.handleLogout, name='handleLogout'),
    path("contact", views.Contact, name='Contact'),
]

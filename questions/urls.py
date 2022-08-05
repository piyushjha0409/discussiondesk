from django.contrib import admin
from django.urls import path
from questions import views 

urlpatterns = [
    path('postComment', views.postComment, name="postComment"),
    path('', views.questions, name="questions"),
    path('<str:slug>', views.QuesContent, name='QuesContent'),
]
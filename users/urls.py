from django.contrib import admin
from django.urls import path, include
from users.views import CreateUser, ValidateUser, MainPage

urlpatterns = [
    path('login/', ValidateUser, name='login'),  
    path('cadastro/', CreateUser, name='validate'),
]
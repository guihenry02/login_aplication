from django.contrib import admin
from django.urls import path
from users.views import CreateUser, ValidateUser, MainPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', ValidateUser, name='login'),  
    path('cadastro/', CreateUser, name='validate'),
    path('auth/', MainPage, name='mainpage')
]

from django.contrib import admin
from django.urls import path, include
from users.views import CreateUser, ValidateUser, MainPage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", MainPage, name = 'home')
]

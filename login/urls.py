from django.contrib import admin
from django.urls import path, include
from users.views import CreateUser, ValidateUser, MainPage, NotAuthenticatedPage
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", MainPage, name = 'home'),
    path('not_authenticated/', NotAuthenticatedPage, name = 'not_auth' ),
    # Essa view 'logout' já é fornecida pelo django e lida com a lógica do logout. Ela aceita por padrão o método POST, por isso o html está envolvido por um form
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout')
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

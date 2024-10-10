from django.contrib import admin
from django.contrib.auth import admin as admin_auth_django
from .models import Users
from .forms import UserChangeForm, UserCreationForm

@admin.register(Users)
class UsersAdmin(admin_auth_django.UserAdmin):
    """
    Classe de administração personalizada para o modelo 'Users'.
    
    Esta classe herda de 'UserAdmin' do Django e adiciona funcionalidades específicas
    para o gerenciamento de usuários na interface administrativa do Django.
    """
    
    form = UserChangeForm  # Formulário utilizado para edição de usuários existentes
    add_form = UserCreationForm  # Formulário utilizado para criação de novos usuários
    model = Users  # Modelo que esta classe de administração gerencia
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ('Phone', {'fields': ('phone',)}),  # Adiciona o campo 'phone' ao conjunto de campos
    )

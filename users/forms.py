from django import forms as form
from django.contrib.auth import forms
from .models import Users

# Formulário de registro de usuários
class RegistrationForm(form.ModelForm):
    """
    Formulário para registrar novos usuários com validação de nome de usuário único.
    """
    password = form.CharField(widget=form.PasswordInput)

    class Meta:
        model = Users
        fields = ['username', 'password', 'phone', 'email']

    def clean_username(self):
        """
        Verifica se o nome de usuário já existe.
        """
        username = self.cleaned_data.get('username')
        if Users.objects.filter(username=username).exists():
            raise forms.ValidationError("Esse nome de usuário já está cadastrado.")
        return username

# Formulário para alterar dados do usuário
class UserChangeForm(forms.UserChangeForm):
    """
    Formulário para modificar dados de um usuário existente.
    """
    class Meta(forms.UserChangeForm.Meta):
        model = Users

# Formulário para criação de usuário
class UserCreationForm(forms.UserCreationForm):
    """
    Formulário para criar novos usuários.
    """
    class Meta(forms.UserCreationForm.Meta):
        model = Users

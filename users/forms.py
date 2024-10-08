from django import forms as form
from django.contrib.auth import forms
from .models import Users

class RegistrationForm(form.ModelForm):
    password = form.CharField(widget=form.PasswordInput)

    class Meta:
        model = Users
        fields = ['username', 'password', 'phone', 'email'] 
    
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if Users.objects.filter(username=username).exists():
            raise forms.ValidationError("Esse nome de usuário já está cadastrado. Por favor, escolha outro.")

        return username
    
class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Users

class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Users
        

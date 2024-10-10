from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    # Esse modelo herda da classe AbstractUser, que é um modelo pré-existente que contém as informações do model User padrão do Django, no entanto, adicionamos mais um campo nela, o phone
    phone = models.CharField(max_length=50)
    

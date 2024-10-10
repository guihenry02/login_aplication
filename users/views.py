from django.shortcuts import render, redirect
from .forms import RegistrationForm  # Importa o formulário de registro criado no forms.py
from django.contrib.auth import authenticate, login  # Ferramentas de autenticação e login do Django
from django.contrib import messages  # Biblioteca para exibir mensagens 
from .models import Users  # Importa o modelo de usuários criados no models.py
from django.contrib.auth.decorators import login_required  # Decorador que exige que o usuário esteja logado para a visualização da página

# Função para criar um novo usuário
def CreateUser(request):
    """
    - Se o método da requisição for 'POST', os dados do formulário são validados.
    - Se os dados forem válidos, um novo usuário é criado no banco de dados usando o modelo 'Users'.
    - Após a criação do usuário, o sistema redireciona para a página de login.
    - Se a requisição não for 'POST', apenas renderiza o formulário de cadastro.
    """
    form = RegistrationForm()  # Inicializa o formulário de registro 
    if request.method == "POST":
        form = RegistrationForm(request.POST)  # Preenche o formulário com os dados do POST
        if form.is_valid():  # Valida os dados do formulário
            # Cria um novo usuário com os dados fornecidos
            user = Users.objects.create_user(
                # O form.cleaned_data extrai e limpa os dados do formulário
                email=form.cleaned_data['email'],  
                username=form.cleaned_data['username'],  
                password=form.cleaned_data['password'],  
                phone=form.cleaned_data['phone']  
            )
            return redirect('login')  # Redireciona o usuário para a página de login após o cadastro
    return render(request, 'users/cadastro.html', {'form': form})  # Renderiza a página de cadastro com o formulário preenchido com as informações anteriores, caso algum dado não tenha sido validado


# Função para validar o login do usuário
def ValidateUser(request):
    """
    Esta função lida com a validação do login do usuário.

    - Se o método da requisição for 'POST', tenta autenticar o usuário com as credenciais fornecidas.
    - Se as credenciais forem válidas, o usuário é autenticado e redirecionado para a página inicial ('home').
    - Se as credenciais forem inválidas, uma mensagem de erro é exibida.
    - Se a requisição não for 'POST', renderiza a página de login com o formulário.
    """
    if request.method == "POST":
        username = request.POST.get('username')  # Obtém o nome de usuário do formulário
        password = request.POST.get('password')  # Obtém a senha do formulário
        user = authenticate(username=username, password=password)  # Tenta autenticar 
        if user:  # Se o usuário for autenticado
            login(request, user)  # Faz o login do usuário
            return redirect('home')  # Redireciona para a página inicial
        else:
            # Se a autenticação falhar, exibe uma mensagem de erro
            messages.error(request, 'Credenciais inválidas. Tente novamente.')
    
    form = RegistrationForm()  # Inicializa um formulário
    return render(request, 'users/login.html', {'form': form})  # Renderiza a página de login com o formulário vazio 


# Função para renderizar a página principal, apenas para usuários autenticados
@login_required(login_url='not_authenticated/')  # Exige que o usuário esteja logado para acessar esta função
def MainPage(request):
    """
    Esta função renderiza a página principal, mas só pode ser acessada por usuários autenticados.
    """
    return render(request, 'users/auth.html')  

# Função para renderizar a página para usuários não autenticados
def NotAuthenticatedPage(request):
    """
    Esta função renderiza uma página que só pode ser acessada por usuários não autenticados.
    """
    if request.user.is_authenticated:  # Se o usuário estiver autenticado
        return redirect('home')  # Redirecione-o para a página principal
    return render(request, 'users/not_authenticated.html')

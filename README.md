#Sistema de Login 

Esse é um pequeno projeto que utiliza algumas ferramentas basicas do django, criado com o intuito de entender melhor o framework Django.
O projeto visa a utilização de usar outras ferramentas em conjunto ao Django como o Tailwind, framework de css.

## Instalação
1. Crie um diretório para o projeto e inicie uma máquina virtual
   mkdir (nome do seu repositório)
   python3 -m venv (nome do seu ambiente virtual) - Para criar um ambiente
   source *nome do seu projeto*/bin/activate - Para iniciar a maquina virtual
   
2. Já dentro da sua pasta, crie um clone do projeto:
   git clone https://github.com/guihenry02/login_aplication.git

3. Instale as dependencias do projeto por meio do requirements.txt:
   pip install -r requirements.txt

4. Na pasta theme, acesse o diretório static_src e baixe as dependencias do node, para habilitar o funcionamento correto do tailwind
   npm install

## Utilização

1. Após a instalação bem sucedida do projeto, gere as migrações dos modelos do django:
   python manage.py migrate
2. Para ter acesso ao painel admin do django, crie um superuser:
   python manage.py createsuperuser
3. Por fim, para que o tailwind compile seu css em tempo real, rode o comando:
   **python manage.py tailwind start

   


   

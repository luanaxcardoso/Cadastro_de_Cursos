## Configuração do Ambiente e Projeto

*** Projeto principal --> (projeto_womakers) ***

*** Com 3 aplicativos --> (base, cursos, rest_api) ***

////////////////////////////////////////////////////////////////////////////////////

# cd Desktop

# pip install virtualenv

# python -m venv cadastro_de_cursos

# .\Scripts\activate

# cd cadastro_de_cursos

# pip install django

# django-admin startproject projeto_womakers .

# python manage.py runserver 

# python manage.py startapp base

*** baixar pasta static do bootstrap ***

*** adicionar arquivos html ***

*** views.py  e urls.py ***

*** settings.py e cadastrar base,bootstrap-v5 ***

 # pip install django-bootstrap-v5

 # python manage.py makemigrations *** vai criar um arquivo de migração ***

# python manage.py migrate *** vai criar o banco de dados ***

# python manage.py createsuperuser

# dados ficticios para teste

*** def em models.py precisa ficar alinhada com a classe para aparecer no admin os nomes dos objetos corretamente ***

////////////////////////////////////////////////////////////////////////////////////

Configuração do Aplicativo de Cursos

.\Scripts\activate

# criar pasta cursos 
cadastrar cursos em settings.py

# criar arquivo models.py, views.py e urls.py em cursos
# criar arquivo urls.py em cursos
http://127.0.0.1:8000/curso/criar_curso/


///////////////////////////////////////////////////////////////////////////////////
Configuração do Cache e do Django REST Framework

Django cache framework 
[Documentação](https://docs.djangoproject.com/en/3.2/topics/cache/)

# pip install redis (se quiser usar o redis como cache)
Após instalar ir em settings.py para cadastrar o 'CACHE'

outra opção é usar o cache do próprio django
inserir cache_page em views.py (Foi usado nessa aplicação)

////////////////////////////////////////////////////////////////////////////////////

.\Scripts\activate
# pip install djangorestframework
Em settings.py adicionar 'rest_framework' em INSTALLED_APPS

# python manage.py startapp rest_api 
Para criar a pasta da aplicação
Em settings.py adicionar 'rest_api' em INSTALLED_APPS

////////////////////////////////////////////////////////////////////////////////////
Configuração da API Django

São necessários os seguintes arquivos para criar uma API

serializers.py
views.py
urls.py

////////////////////////////////////////////////////////////////////////////////////

Testes e Execução do Servidor
# pip install pytest-django
# pip install pytest
rodar o teste
# pytest
# pip install model_bakery

////////////////////////////////////////////////////////////////////////////////////

# Para rodar o servidor

**1º**   .\Scripts\activate

**2º**   python manage.py runserver  

**3º**   Escolher um dos links abaixo para acessar o servidor

(http://127.0.0.1:8000/)

(http://127.0.0.1:8000/curso/criar_curso/)

(http://127.0.0.1:8000/admin)

Para acessar o admin (usuário e senha  apenas para teste, não usar em produção)
admin -- luana
senha -- 1234

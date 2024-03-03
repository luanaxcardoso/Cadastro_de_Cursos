from django.shortcuts import render
from django.http import HttpResponse
from base.forms import CadastroForm
from base.models import Cadastro

# def inicio(request):
    
#     return render(request, 'inicio.html')

# def cadastro(request):
#     sucesso = False
#     form = CadastroForm(request.POST or None)
#     if form.is_valid():
#             sucesso = True
#             form.save()
#     contexto = {
#         'form': form,
#         'sucesso': sucesso
#     }    
#     return render(request, 'cadastro.html', contexto) 

def inicio(request):
    cadastros = Cadastro.objects.all()  # Recupera todos os cadastros do banco de dados
    contexto = {
        'cadastros': cadastros
    }
    return render(request, 'inicio.html', contexto)

def cadastro(request):
    sucesso = False
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    contexto = {
        'form': form,
        'sucesso': sucesso
    }    
    return render(request, 'cadastro.html', contexto) 
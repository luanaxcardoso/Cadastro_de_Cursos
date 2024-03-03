from django.contrib import admin
from base.models import Cadastro

@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'data']
    search_fields = ['nome', 'email', 'data']
    list_filter = ['nome', 'email']
    list_per_page = 10


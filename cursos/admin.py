from django.contrib import admin
from cursos.models import Curso

@admin.register(Curso)

class CursoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "nivel", "carga_horaria", "data_do_curso")
    list_filter = ("titulo", "nivel", "data_do_curso")
    search_fields = ("titulo", "descricao")
    date_hierarchy = "data_do_curso"
    ordering = ("data_do_curso", "titulo")
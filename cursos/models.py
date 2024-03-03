from django.db import models

# Create your models here.
class Curso(models.Model):
    niveis_de_curso = [
        ("Iniciante", "Básico"),
        ("Intermediário", "Intermediário"),
        ("Avançado", "Avançado"),
    ]
    titulo = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50, choices=niveis_de_curso, default=0)
    carga_horaria = models.IntegerField()
    data_do_curso = models.DateField(help_text="Use o formato: YYYY-MM-DD")
    descricao = models.TextField()

    def __str__(self):
        return f'{self.titulo}: {self.data_do_curso} - {self.carga_horaria}'
    
    class Meta:
        verbose_name = "Cadastro de Curso"
        verbose_name_plural = "Cadastros de Cursos"
        ordering = ["-data_do_curso", "titulo"]
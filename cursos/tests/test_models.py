from datetime import date
from model_bakery import baker
from cursos.models import Curso
import pytest

@pytest.fixture # faz com que o teste seja executado apenas uma vez
def curso():
    curso = baker.make(
        Curso, 
        titulo='Python para Devs', 
        data_do_curso= date.today(),
        carga_horaria=20
    )
    return curso

@pytest.mark.django_db
def test_str_deve_retornar_string(curso):
    assert str(curso) == 'Python para Devs: 2024-02-28 - 20'
    

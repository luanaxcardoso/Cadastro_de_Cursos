from django.contrib import admin
from django.urls import path, include
from base.views import inicio, cadastro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name = 'inicio'), 
    path('cadastro/', cadastro, name = 'cadastro'), 
    path('curso/', include('cursos.urls', namespace = 'cursos')), 
    path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework') ),
    path('api/', include('rest_api.urls', namespace = 'api')),
]

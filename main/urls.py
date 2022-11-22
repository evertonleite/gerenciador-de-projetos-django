from django.urls import path
from .views import analista, atividade, programador, projeto, letra

urlpatterns = [
    path('projetos/', projeto, name='projeto'),
    path('analistas/', analista, name='analista'),
    path('programadores/', programador, name='programador'),
    path('atividades/', atividade, name='atividades'),
    path('letras/<str:letras>', letra, name='letras'),
]
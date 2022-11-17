from django.urls import path
from .views import analista, atividade, programador, projeto

urlpatterns = [
    path('projetos/', projeto, name='projeto'),
    path('analistas/', analista, name='analista'),
    path('programadores/', programador, name='programador'),
    path('atividades/', atividade, name='atividades'),
]
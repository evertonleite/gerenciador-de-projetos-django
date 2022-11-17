from django.shortcuts import render
from .models import Analista, Atividade, Programador, Projeto

def analista(request):
    analistas = Analista.objects.all()
    context = {
        'analistas': analistas
    }
    return render(request, 'analista.html', context )

def atividade(request):
    atividades = Atividade.objects.all()
    context = {
        'atividades': atividades
    }
    return render(request, 'atividade.html', context)

def programador(request):
    programadores = Programador.objects.all()
    if request.method == 'GET':
        context = {
            'programadores': programadores
        }
    return render(request, 'programador.html', context )

def projeto(request):
    projetos = Projeto.objects.all()
    if request.method == 'GET':
        context = {
            'projetos': projetos
        }
    return render(request, 'projeto.html', context)
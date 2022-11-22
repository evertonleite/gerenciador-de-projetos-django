from django.shortcuts import render
from .models import Analista, Atividade, Programador, Projeto
from .forms import AnalistaForm, AtividadeForm, ProgramadorForm, ProjetoForm

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

def letra(request, letras):
    maiuscula = letras.upper()
    tamanho = len(letras)    
    context = {
        'maiuscula': maiuscula,
        'tamanho': tamanho
    }
    return render(request, 'letras.html', context)

def cadastroAnalista(request):
    form = AnalistaForm()
    return render(request, 'cadastroAnalista.html', { 'form': form})

def cadastroAtividade(request):
    form = AtividadeForm()
    return render(request, 'cadastroAtividade.html', { 'form': form})

def cadastroProgramador(request):
    form = ProgramadorForm()
    return render(request, 'cadastroProgramador.html', { 'form': form})

def cadastroProjeto(request):
    form = ProjetoForm()
    return render(request, 'cadastroProjeto.html', { 'form': form})
    
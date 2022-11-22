from django import forms
from .models import Analista, Atividade, Programador, Projeto

class AnalistaForm(forms.ModelForm):
    class Meta:
        model = Analista
        fields = '__all__'
 
class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = '__all__'
        
class ProgramadorForm(forms.ModelForm):
    class Meta:
        model = Programador
        fields = '__all__'
                
class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'
        


        
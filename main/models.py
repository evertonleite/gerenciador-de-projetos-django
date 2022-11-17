from django.db import models

class Projeto(models.Model):
    data_inicio = models.DateField()
    nome_projeto = models.CharField(max_length=100)
    finalidade_projeto = models.TextField(max_length=300)
    
    def __str__(self):
        return self.nome_projeto
    
class Analista(models.Model):
    nome_analista = models.CharField(max_length=52)
    
    def __str__(self):
        return self.nome_analista
    
class Programador(models.Model):
    nome_programador = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome_programador
    
class Atividade(models.Model):
    nome_atividade = models.CharField(max_length=100)
    data_inicio_atividade = models.DateField()
    descricao_atividade = models.TextField(max_length=300)
    cod_analista = models.ForeignKey(Analista, on_delete=models.CASCADE)
    cod_programador = models.ForeignKey(Programador, on_delete=models.CASCADE)
    cod_projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome_atividade
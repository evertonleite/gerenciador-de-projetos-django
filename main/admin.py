from django.contrib import admin

from main.models import Projeto
from main.models import Analista
from main.models import Programador
from main.models import Atividade

admin.site.register(Projeto)
admin.site.register(Analista)
admin.site.register(Programador)
admin.site.register(Atividade)
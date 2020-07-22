from django.contrib import admin
from core.models import Evento # importa classe Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao') # cria lista que exibe elementos dos eventos
    list_filter = ('titulo', 'usuario', 'data_evento',) # cria lista de filtro por titulo, usuário e data

admin.site.register(Evento, EventoAdmin) # registra tabela Evento e lista EventoAdmin


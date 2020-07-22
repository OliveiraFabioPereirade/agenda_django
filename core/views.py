from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here.



def eventos(request, titulo_evento): # função que recebe requisição e título
     consulta = Evento.objects.get(titulo = titulo_evento) # procura por evento que tenha o título recebido
     descricao = consulta.descricao # pega a descrição do evento encontrado
     return HttpResponse(descricao) # retorna a descrição na resposta da requisição


def lista_eventos(request): # função que
    usuario = request.user # obtém o nome do usuário que está fazendo a requisição
    evento = Evento.objects.filter(usuario= usuario) # obtém uma lista com todos os eventos do usuario da requisiçãop
    dados = {'eventos' : evento} # cria um dicionário com a lista de eventos
    return render(request, 'agenda_django.html', dados) # renderiza a página 'agenda_django.html' e passa o dicionário
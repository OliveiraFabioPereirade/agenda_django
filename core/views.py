from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here.



def eventos(request, titulo_evento): # função que recebe requisição e título
     consulta = Evento.objects.get(titulo = titulo_evento) # procura por evento que tenha o título recebido
     descricao = consulta.descricao # pega a descrição do evento encontrado
     return HttpResponse(descricao) # retorna a descrição na resposta da requisição


def lista_eventos(request): # função que
    evento = Evento.objects.get(id=1) # obtém o primeiro evento (íd=1)
    response = {'evento' : evento} # cria um dicionário com o evento
    return render(request, 'agenda_django.html', response) # renderiza a página 'agenda_django.html' e passa o dicionário
from django.shortcuts import render, HttpResponse
#                                         |
#                                         +--> transforma argumento em resposta HTTP
from core.models import Evento
from django.contrib.auth.decorators import login_required  # decorador (começa com @) que exige autênticação para função

# Create your views here.


def eventos(request, titulo_evento): # função que recebe requisição e título
     consulta = Evento.objects.get(titulo = titulo_evento) # procura por evento que tenha o título recebido
     descricao = consulta.descricao # pega a descrição do evento encontrado
     return HttpResponse(descricao) # retorna a descrição na resposta da requisição


@login_required(login_url='/login/')  # exige autênticação para função, sem autenticação: direciona para a página '/login/'
def lista_eventos(request): # função que
    evento = Evento.objects.all() # obtém uma lista com todos os eventos
    dados = {'eventos' : evento} # cria um dicionário com a lista de eventos
    return render(request, 'agenda_django.html', dados) # renderiza a página 'agenda_django.html' e passa o dicionário

def login_user(request):    # função que
    return render(request, 'login.html') #renderiza a página 'login.html'
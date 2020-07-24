from django.shortcuts import render, HttpResponse, redirect
#                              |          |           |
#                              |          |           +--> redireciona requisição para outra rota
#                              |          +--> transforma argumento em resposta HTTP
#                              +--> renderiza elementos HTML

from core.models import Evento
from django.contrib.auth.decorators import login_required  # decorador (começa com @) que exige autênticação para função
from django.contrib import messages # permite passar mensagens
from django.contrib.auth import authenticate, login, logout
#                                   |           |       |
#                                   |           |       +--> permite logout
#                                   |           +--> permite login
#                                   +--> permite autenticação

# Create your views here.


@login_required(login_url='/login/')  # exige autênticação para função, sem autenticação: direciona para a página '/login/'
def eventos(request, titulo_evento): # função que recebe requisição e título
     consulta = Evento.objects.get(titulo = titulo_evento) # procura por evento que tenha o título recebido
     descricao = consulta.descricao # pega a descrição do evento encontrado
     return HttpResponse(descricao) # retorna a descrição na resposta da requisição


@login_required(login_url='/login/')  # exige autênticação para função, sem autenticação: direciona para a página '/login/'
def lista_eventos(request): # função que
    usuario = request.user # pega o nome do usuário na requisição
    evento = Evento.objects.filter(usuario= usuario) # obtém uma lista dos eventos do usuário da requisição
    dados = {'eventos' : evento} # cria um dicionário com a lista de eventos
    return render(request, 'agenda_django.html', dados) # renderiza a página 'agenda_django.html' e passa o dicionário

@login_required(login_url='/login/')  # exige autênticação para função, sem autenticação: direciona para a página '/login/'
def delete_evento(request,id_evento): # função que
    usuario = request.user # pega o nome do usuário na requisição
    evento = Evento.objects.get(id=id_evento) # pega o evento com id igual ao id_evento
    if usuario == evento.usuario: # se usuario da requisição é o mesmo do evento:
        evento.delete() # apaga o evento com id igual ao id_evento
    return redirect('/')  # redireciona para a página principal





@login_required(login_url='/login/')  # exige autênticação para função, sem autenticação: direciona para a página '/login/'
def submit_evento(request):  # função que
    if request.POST:  # se requisição     for POST:
        titulo = request.POST.get('titulo') # pega o valor do titulo no POST da requisição
        data_evento = request.POST.get('data_evento') # pega o valor do data_evento no POST da requisição
        descricao = request.POST.get('descricao') # pega o valor do descricao no POST da requisição
        local = request.POST.get('local') # pega o valor do local no POST da requisição
        usuario = request.user # pega o valor do usuario na requisição
        Evento.objects.create(titulo= titulo,
                              data_evento= data_evento,
                              descricao= descricao,
                              usuario= usuario,
                              local= local)
    return redirect('/') # redireciona para a página principal

@login_required(login_url='/login/')  # exige autênticação para função, sem autenticação: direciona para a página '/login/'
def evento(request):  # função que
    return render(request, 'evento.html') # renderiza a página 'evento.html'

def login_user(request):    # função que
    return render(request, 'login.html') #renderiza a página 'login.html'

def submit_login(request):  # função que
    if request.POST:  # se requisição     for POST:
        username = request.POST.get('username') # pega o valor do username no POST da requisição
        password = request.POST.get('password') # pega o valor do password no POST da requisição
        usuario = authenticate(username= username, password= password) # tenta autenticar usuário
        if usuario is not None: # se autenticação não retornou vazio
            login(request, usuario) # realiza login do usuário
        else:
            messages.error(request, "Usuário ou senha invalidos!") # informa que o usuário ou a senha estão errados
    return redirect('/') # redireciona para a página principal

def logout_user(request):  # função que
    logout(request) # realiza logout do usuário
    return redirect('/')  # redireciona para a página principal


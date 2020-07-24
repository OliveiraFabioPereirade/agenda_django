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
        id_evento = request.POST.get('id_evento') # pega o valor do id_evento no POST da requisição
        if id_evento: # se id_evento não for vazio, é uma alteração, então:
            evento = Evento.objects.get(id= id_evento) # pega o evento com id igual ao id_evento
            if usuario == evento.usuario:  # se usuario da requisição é o mesmo do evento:
                evento.titulo = titulo            # altera campo titulo
                evento.data_evento = data_evento  # altera campo data_evento
                evento.descricao = descricao      # altera campo descricao
                evento.local = local              # altera campo titulo
                evento.save() # atualiza evento (este método permite validar alterações antes de atualizar
            # Evento.objects.filter(id= id_evento).update(titulo= titulo,            #atualiza evento e altera campos: titulo
            #                                             data_evento= data_evento,  #                                 data_evento
            #                                             descricao= descricao,      #                                 descricao
            #                                             local= local)              #                                 local
        else:         # se id_evento     for vazio, é uma inserção, então:
            Evento.objects.create(titulo= titulo,            #cria evento e preenche campos: titulo
                                  data_evento= data_evento,  #                               data_evento
                                  descricao= descricao,      #                               descricao
                                  usuario= usuario,          #                               usuario
                                  local= local)              #                               local
    return redirect('/') # redireciona para a página principal

@login_required(login_url='/login/')  # exige autênticação para função, sem autenticação: direciona para a página '/login/'
def evento(request):  # função que
    id_evento = request.GET.get('id') # pega o valor do id_evento no GET da requisição
    # print(id_evento) #exibe valor do id_evento
    dados = {} # inicialmente não há dados, para o caso de uma inserção de eventos
    if id_evento: #se há id_evento, é uma alteração, então:
        dados ['evento']= Evento.objects.get(id=id_evento) # preenche 'dados'^; com dados do evento identificado pelo id_evento
    return render(request, 'evento.html', dados) # renderiza a página 'evento.html' e passa dados do evento

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


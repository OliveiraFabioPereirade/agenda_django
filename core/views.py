from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here.



def eventos(request, titulo_evento):
    # consulta = Evento.objects.get(titulo = titulo_evento)
    # local = objeto.consulta
    # return HttpResponse(local)
    return HttpResponse('Hello World!')

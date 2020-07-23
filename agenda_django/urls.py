"""agenda_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eventos/<titulo_evento>', views.eventos),  # cria rota 'titulo_evento/' para executar 'eventos'
    path('agenda/', views.lista_eventos), # cria rota 'agenda/' para executar 'lista_eventos'
    path('agenda/evento/', views.lista_evento), # cria rota 'agenda/evento' para cadastrar eventos
    path('', RedirectView.as_view(url= '/agenda/')),  # redireciona para rota '/agenda/' como se fosse uma view
    path('login/', views.login_user),  # cria rota 'login/' para permitir login do usuário
    path('login/submit', views.submit_login),  # cria rota 'login/submit/' para tratar login do usuário
    path('logout/', views.logout_user),  # cria rota 'logout/' para permitir logout do usuário

]

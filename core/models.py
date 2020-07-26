from django.db import models
from django.contrib.auth.models import User # importa lista usuários do django
from datetime import datetime  # permite obter hora e data atual

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100) # máximo 100 caracteres, não pode ser branco ou nulo
    descricao = models.TextField(blank=True, null=True) # não tem limite de caracteres, pode ser branco ou nulo
    data_evento = models.DateTimeField(verbose_name='Data do evento') #campo de data e hora, não pode ser nulo, e customiza nome
    data_criacao = models.DateTimeField(auto_now=True) #campo de data e hora, pega hora da inserção automaticamente
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # acrescenta foreign key com usuários do django
                                                                # caso o usuário seja deletado, seus eventos também serão
    local = models.CharField(max_length=100, blank=True, null=True)  # máximo 100 caracteres, pode ser branco ou nulo

# para migrar esta tabela sem adicionar ao banco de dados, executar:
# python manage.py makemigrations core
#                                      a opção core indica que deve migrar apenas o que esta na aplicação core
# isto gera um arquivo  core\migrations\0001_initial.py

# para ver o código SQL da migração, executar:
# python manage.py sqlmigrate core 0001
# o resultado é:
# CREATE TABLE "core_evento" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "titulo" varchar(100) NOT NULL,
# "descricao" text NULL, "data_evento" date NOT NULL, "data_criacao" date NOT NULL);

# notar que a tabela é chamada "core_evento" por padrão
# para forçar um nome é preciso acrescentar a classe abaixo, apagar o arquivo 0001_initial.py, e reexecutar:
# python manage.py makemigrations core

    class Meta:
        db_table = 'evento'

# para ver o novo código SQL da migração, reexecutar:
# python manage.py sqlmigrate core 0001
# o resultado é:
# CREATE TABLE "evento" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "titulo" varchar(100) NOT NULL,
# "descricao" text NULL, "data_evento" date NOT NULL, "data_criacao" date NOT NULL);

# notar que a tabela é chamada "evento" agora

# para implementar esta tabela no banco de dados, executar:
# python manage.py migrate core 0001

# um evento criado até aqui será listado como: Evento object(x), onde x é o sua ordem de criação
# para que um evento seja listato com nome do seu titulo, devemos acrescentar a função abaixo:

    def __str__(self):
        return self.titulo # sempre que alguém chamar este objeto, será retornado o nome do titulo

# os campos data_evento e data_criacao estavam apenas como DateField e não como DateTimeField,
# para alterá-los, além de mudar o tipo neste arquivo, deve-se parar a aplicação e executar:
# python manage.py makemigrations core                  (cria o 0002)
# python manage.py sqlmigrate core 0002                 (mostra as modificações)
# python manage.py migrate core 0002                    (aplica as modificações)
# após isto, os campos DateTimeField dos eventos existentes estarão em branco,
# mas é possível editá-los e então exibirão data e hora como devia ser

# para transformar a aplicação em multiusuário, insere uma foreign key com usuários do django na tabela eventos,
# parar a aplicação e e executar:
# python manage.py makemigrations core                  (cria o 0003)
#       perguntará se manterá campos já existentes: responder 1 para mantê-los
#       depois, digitar 1 para preencher campos vazios e atribuir eventos existentes ao admin'
# python manage.py sqlmigrate core 0003                 (mostra as modificações)
# python manage.py migrate core 0003                    (aplica as modificações)

    def get_data_evento(self): # cria função
        return self.data_evento.strftime('%d/%m/%y %H:%M hrs.') # que retorna a data e hora do evento formatadas

# para guardar o local do evento, insere o campo 'local' na tabela eventos,
# parar a aplicação e e executar:
# python manage.py makemigrations core                  (cria o 0004)
# python manage.py sqlmigrate core 0004                 (mostra as modificações)
# python manage.py migrate core 0004                    (aplica as modificações)

    def get_data_input_evento(self): # cria função
        return self.data_evento.strftime('%Y-%m-%dT%H:%M') # que retorna a data e hora do evento formatadas para datetime-local

    def get_evento_atrasado(self):  # cria função que
        if self.data_evento < datetime.now():  # se data_evento for anterior a data atual:
            return True                        # retorne True
        else:                                  # senão:
            return False                       # retorne False

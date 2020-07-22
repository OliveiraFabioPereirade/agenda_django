from django.db import models

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100) # máximo 100 caracteres, não pode ser branco ou nulo
    descricao = models.TextField(blank=True, null=True) # não tem limite de caracteres, pode ser branco ou nulo
    data_evento = models.DateField() #campo de data e hora, não pode ser nulo
    data_criacao = models.DateField(auto_now=True) #campo de data e hora, pega hora da inserção automaticamente

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


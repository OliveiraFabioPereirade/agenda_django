# agenda_django

App desenvolvido durante o curso:

### Desenvolvimento para Internet e Banco de Dados com Python e Django

![](https://i.imgur.com/fpUQOLd.png?1)

Oferecido por: 

### Digital Innovation One

Ministrado por:

### Rafael Galleani

---

## Fases do projeto:

Cria uma aplicação agenda em Python utilizando o framework Django.

Todas as fases do projeto foram separadas por commits:

-	1	-	Cria estrutura básica da aplicacao
-	2	-	Cria tabelas padrão, super usuário e usuários
-	3	-	Tabela Evento: cria, migra para SQL, implementa no banco de dados, registra, força nome e identifica eventos por titulo
-	4	-	Tabela Evento: adiciona lista de parâmetros dos eventos e persolaliza nome de parâmetros
-	5	-	Tabela Evento: corrige campos que mostravam apenas data para mostrarem data e hora
-	6	-	Tabela Evento: acrescenta campo que associa evento ao usuário
-	7	-	Cria filtros de eventos por título, usuário e data
-	8	-	Tenta criar uma rota que retorne o local do evento através do nome do evento
-	9	-	Criar rota que retorne a descrição do evento através do titulo do evento, e cria rota agenda com passagem de parâmetros
-	10	-	Rota agenda: exibe lista com titulo e data de todos os eventos
-	11	-	Rota agenda: exibe lista com titulo e data de todos os eventos em tópicos
-	12	-	Rota agenda: formata hora exibida na lista de tópicos
-	13	-	Rota agenda: filtra eventos na lista por usuário
-	14	-	Rota agenda: padroniza header e footer das páginas
-	15	-	Rota http://127.0.0.1:8000/ é redirecionada para rota http://127.0.01:8000/agenda (primeira forma)
-	16	-	Exige autenticação para a rota '\agenda'
-	17	-	Sem autenticação, rota '\agenda' é redirecionada para página de login
-	18	-	Na rota '\login', autentica e loga usuário, se nome e senha estiverem corretos
-	19	-	Permite logout na página'agenda'
-	20	-	Trata usuário ou senha inválidos no login
-	21	-	Cria rota '\agenda\evento' para cadastrar eventos
-	22	-	Cria botão na página 'agenda' que direciona para página 'evento'
-	23	-	Cria formulário para cadastrar evento e botões salvar e cancelar na página 'evento'
-	24	-	Realiza cadastramento de eventos por usuário
-	25	-	Acrescenta campo 'local' na tabela 'Eventos' e permite sua exibição e edição
-	26	-	Cria rota '\agenda\evento\delete\id' para apagar evento identificado pelo seu id
-	27	-	Cria rota '\agenda\evento\delete\id' apaga apenas eventos do usuario logado
-	28	-	Cria botão excluir evento
-	29	-	Cria botão editar evento (primeira forma)
-	30	-	Cria botão editar evento (segunda forma)
-	31	-	Exibe apenas eventos que tennham ocorrido há menos que uma hora
-	32	-	Escreve em vermelho os eventos que estejam atrasados
-	33	-	Trata erro ao deletar evento que não existe ou não pertence ao usuário
-	34	-	Cria rota 'agenda/lista/' para retornar lista de eventos no formato Json
-	35	-	Altera rota para 'agenda/lista/id' e assim retornar lista de eventos do usuario (id) como uma API

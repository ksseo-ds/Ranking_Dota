from dotenv import load_dotenv
from front.front import *
from services.steam_api import Requisicao
from models.model_jogadores import Jogadores
from models.db import db_dota

load_dotenv()
#steamKey = os.getenv('API_STEAM')
#inicializando o Menu e atribuindo o id_steam do Ranking
menu = Menu()
id_ranking = menu.menu_inicial()

#inicializando a lista de amigos da api_steam
lista_amigos = Requisicao()
lista_amigos = lista_amigos.atualizar_lista_amigos(id_ranking=id_ranking)

# Requisitando o Tier da lista dos amigos do ranking
lista_amigos = Requisicao.atualizar_tier(lista_amigos) # lembrar de tirar a restrição 6 amigos no steam_api.pi linha 36

# a variável lista_amigos, é uma lista que contem dicionários, e cada dicionário é um jogador



### Começa a inclusão no BD


db_dota.connect()
db_dota.create_tables([Jogadores], safe = True)

Jogadores.adicionar_ao_bd(lista_amigos)

db_dota.close()
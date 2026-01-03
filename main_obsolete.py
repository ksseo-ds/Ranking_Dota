from dotenv import load_dotenv
from front.front import *
from services.steam_api import Requisicao
from models.model_jogadores import Jogadores
from models.model_tiers import Tiers
from models.model_historico_tiers import Historico_tier
from models.db import db_dota



load_dotenv()
#steamKey = os.getenv('API_STEAM')
#inicializando o Menu e atribuindo o id_steam do Ranking
menu = Menu()
id_ranking = menu.menu_inicial()

db_dota.connect()
db_dota.create_tables([Jogadores, Tiers, Historico_tier], safe = True)

#inicializando a lista de amigos da api_steam
lista_amigos = Requisicao()
lista_amigos = lista_amigos.atualizar_lista_amigos(id_ranking=id_ranking)

# Requisitando o Tier da lista dos amigos do ranking
lista_tier = Requisicao.atualizar_tier(lista_amigos) # lembrar de tirar a restrição 6 amigos no steam_api.pi linha 36
for i in lista_tier:
    Historico_tier.incluir_tier_bd(i)
# a variável lista_amigos, é uma lista que contem dicionários, e cada dicionário é um jogador



### Começa a inclusão no BD



Jogadores.adicionar_ao_bd(lista_amigos)

db_dota.close()



###
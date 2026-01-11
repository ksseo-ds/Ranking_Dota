import os
from dotenv import load_dotenv
from models.db import db_dota
from models.model_jogadores import Jogadores
from models.model_tiers import Tiers
from models.model_sessao import Sessao
from models.model_historico_tiers import Historico_tier
from models.model_open_dota_billing import Open_dota_billing
from services.jogador_service import construir_jogador
from services.steam_api_service import SteamApiService 

load_dotenv()
# Bd table creations if doesn't exsixt
db_dota.create_tables([Jogadores, Sessao, Tiers, Historico_tier])

# Populate Tiers in the Bd if doesn't exists
Tiers.popular_tabela_tiers()

#creating session in bd.sessao
sessao = Sessao.gerar_nova_sessao()

#the steam_id of the target to rank its friends
ranking = os.getenv('RANKING_STEAM') 
# creating the friends list of the target 
lista_de_jogadores = SteamApiService().listar_amigos_raw(id_ranking=ranking)['amigos']


#constructing the player and inserting in the BD
for id_jogador in lista_de_jogadores:
    jogador = construir_jogador(steam_id = id_jogador)
    jogador['dados']['sessao'] = sessao

    steam_id = jogador['dados']['steamid']
    personaname = jogador['dados']['personaname']
    profilestate = jogador['dados']['communityvisibilitystate']
    avatar = jogador['dados']['avatarfull']
    tier = jogador['dados']['tier']
    open_dota_billing = jogador['billing'] #  Crud para Billing
    print(jogador['dados'])

    #CRUD player 
    Jogadores.adicionar_jogador(steam_id=steam_id,
                                personaname=personaname,
                                profilestate=profilestate,
                                avatar=avatar
                                )
    print('atualizado')
    #CRUD Tier of the player
    Historico_tier.incluir_tier_bd(jogador=jogador['dados'])

    #CRUD Billing
    Open_dota_billing.open_dota_bill(session_id=sessao,requisition_billing=open_dota_billing)

    
'''
todo:
[] Verificação se um jogador já foi atualizado hoje antes de fazer o Crud


'''

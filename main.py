import os
from dotenv import load_dotenv
from db import db_dota
from models.model_player import Player
from models.model_tiers import Tiers
from models.model_session import Sessao
from models.model_tiers_history import TierHistory
from models.model_open_dota_billing import OpenDotaBilling
from services.jogador_service import build_player
from services.steam_api_service import SteamApiService 

load_dotenv()
# Bd table creations if doesn't exsixt
db_dota.create_tables([Player, Sessao, Tiers, TierHistory])

# Populate Tiers in the Bd if doesn't exists
Tiers.pupulate_tier_table()

#creating session in bd.sessao
sessao = Sessao.gerar_nova_sessao()

#the steam_id of the target to rank its friends
ranking = os.getenv('RANKING_STEAM') 
# creating the friends list of the target 
lista_de_jogadores = SteamApiService().raw_friend_list(id_ranking=ranking)['amigos']


#constructing the player and inserting in the BD
for id_jogador in lista_de_jogadores:
    jogador = build_player(steam_id = id_jogador)
    jogador['dados']['sessao'] = sessao

    steam_id = jogador['dados']['steamid']
    personaname = jogador['dados']['personaname']
    profilestate = jogador['dados']['communityvisibilitystate']
    avatar = jogador['dados']['avatarfull']
    tier = jogador['dados']['tier']
    open_dota_billing = jogador['billing'] #  Crud para Billing
    print(jogador['dados'])

    #CRUD player 
    Player.create_update_player(steam_id=steam_id,
                                personaname=personaname,
                                profilestate=profilestate,
                                avatar=avatar
                                )
    print('atualizado')
    #CRUD Tier of the player
    TierHistory.create_update_tier_db(jogador=jogador['dados'])

    #CRUD Billing
    OpenDotaBilling.open_dota_bill(session_id=sessao,requisition_billing=open_dota_billing)

    
'''
todo:
[] Verificação se um jogador já foi atualizado hoje antes de fazer o Crud


'''

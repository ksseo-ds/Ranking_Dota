from dotenv import load_dotenv
import os
from models.db import db_dota
from models.model_jogadores import Jogadores
from models.model_tiers import Tiers
from models.model_sessao import Sessao
from models.model_historico_tiers import Historico_tier
from services.jogador_service import construir_jogador
from services.steam_api_service import SteamApiService 



db_dota.create_tables([Jogadores, Sessao, Tiers, Historico_tier])

Tiers.popular_tabela_tiers()

sessao = Sessao.gerar_nova_sessao()

ranking = '76561198266319437'

lista_de_jogadores = SteamApiService().listar_amigos_raw(id_ranking=ranking)['amigos']



for id_jogador in lista_de_jogadores:
    jogador = construir_jogador(steam_id = id_jogador)
    jogador['dados']['sessao'] = sessao

    steam_id = jogador['dados']['steamid']
    personaname = jogador['dados']['personaname']
    profilestate = jogador['dados']['communityvisibilitystate']
    avatar = jogador['dados']['avatarfull']
    tier = jogador['dados']['tier']

    print(jogador['dados'])

    Jogadores.adicionar_jogador(steam_id=steam_id,
                                personaname=personaname,
                                profilestate=profilestate,
                                avatar=avatar
                                )
    print('atualizado')
    
    Historico_tier.incluir_tier_bd(jogador=jogador['dados'])




import os
from typing import Dict, List, Any
from time import sleep, perf_counter
from services.open_dota_api_service import OpenDotaService
from services.steam_api_service import SteamApiService

def construir_jogador(steam_id: str) -> Dict:
    '''
    Essa função cria um Dicionário com duas keys, na qual temos 'dados', representando os dados do jogador criado, e 'performance' que representa quanto tempo levou para a requisição estar completa nas apis.

    retorno =   { dados : { 
                        steamid : str,
                        personaname : str,
                        communityvisibilitystate : int,
                        avatarfull : str                        
                            },
                performance : float    
                }

    '''
    jogador = SteamApiService().solicitar_dados_amigos(amigo = steam_id)

    if jogador['dados']['communityvisibilitystate'] == 3:
        tier = OpenDotaService().solicita_tier(user_id = steam_id)
    
    else:
        tier = {'tier': None,
                'performance_open_dota': 0 }
    # inclui o tier dentro do dict de dados do jogador
    jogador['dados']['tier'] = tier['tier']

    #soma as performances da API
    jogador['performance'] = jogador.pop('performance_steam')
    jogador['performance'] += tier['performance_open_dota']
    
    

    return jogador





if __name__ == '__main__':

    ranking = "76561198266319437"
    jogador = construir_jogador(steam_id = ranking)


    print(jogador.keys())
    print(jogador)
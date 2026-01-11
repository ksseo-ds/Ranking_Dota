from typing import Dict 
from services.open_dota_api_service import OpenDotaService
from services.steam_api_service import SteamApiService

def build_player(steam_id: str) -> Dict:
    '''
    This function creates a Dictionary with two keys: 'dados' (data), representing the data of the created player, and 'performance', representing how long it took for the request to complete in the APIs.


    return =   { dados : { 
                        steamid : str,
                        personaname : str,
                        communityvisibilitystate : int,
                        avatarfull : str                        
                            },
                performance : float    
                }

    '''
    player = SteamApiService().player_data_request(player = steam_id)

    if player['dados']['communityvisibilitystate'] == 3:
        tier = OpenDotaService().tier_request(user_id = steam_id)
    
    else:
        tier = {'tier': None,
                'performance_open_dota': 0,
                 'billing_open_dota':0 }
    # inclui o tier dentro do dict de dados do jogador
    player['dados']['tier'] = tier['tier']
    player['billing'] = tier['billing_open_dota']
    #soma as performances da API
    player['performance'] = player.pop('performance_steam')
    player['performance'] += tier['performance_open_dota']
    
    

    return player





if __name__ == '__main__':

    ranking = "76561198266319437"
    jogador = build_player(steam_id = ranking)


    print(jogador.keys())
    print(jogador)

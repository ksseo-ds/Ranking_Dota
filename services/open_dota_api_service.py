import os
from typing import Dict, List, Any
import requests
from dotenv import load_dotenv
from time import sleep, perf_counter
#carregando as váriaveis de sistema (chaves de api)
load_dotenv()

class OpenDotaService:

    def __init__(self):
        
        OPENDOTAKEY = os.getenv('OPEN_DOTA_API')
        self.open_dota_key = OPENDOTAKEY


    def steam32_to_steam64(self, steam_id: str) -> str:
        '''
        recebe uma string que seria o steamid de um usuário, para retornar uma string que seria o user_id requerido pela api do open_dota para que faça as demais buscas

        essa função é usada apenas nas funções para chamada de api do open_dota, e não necessita de uso fora desse escopo
        
        '''

        valor_offset = 76561197960265728

        return str(int(steam_id) - valor_offset)
    

    def solicita_tier(self, user_id: str) -> Dict:

        '''
        Recebe um steamid, e retorna o tier desse usuário, junto com a performance da solicitação da api

        retorno = {
            'tier': int,
            'performance_open_dota': float
            }
        '''


        account_id = OpenDotaService().steam32_to_steam64(user_id)

        start_api_call = perf_counter()
        req = requests.get(f'https://api.opendota.com/api/players/{account_id}').json()

        end_api_call = perf_counter()
        performance = round((end_api_call - start_api_call),2)

        
        retorno = {'tier':req.get('rank_tier'),
                   'performance_open_dota': performance
        }


        return retorno 
    
    

if __name__ == '__main__':

    ranking ="76561198266319437"

    tier = OpenDotaService().solicita_tier(user_id=ranking)

    print(tier)

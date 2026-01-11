import os
from typing import Dict
import requests
from dotenv import load_dotenv
from time import perf_counter
#load Env Variables (API KEY)
load_dotenv()

class OpenDotaService:

    def __init__(self):
        
        OPENDOTAKEY = os.getenv('OPEN_DOTA_API')
        self.open_dota_key = OPENDOTAKEY


    def steam32_to_steam64(self, steam_id: str) -> str:
        '''
        This function receives a string that represents a user's steamid, and returns a string that represents the user_id required by the Open_Dota API for subsequent searches.

        This function is only used in functions that call the Open_Dota API and is not needed outside of that scope.
        
        '''

        offset_value = 76561197960265728

        return str(int(steam_id) - offset_value)
    

    def tier_request(self, user_id: str) -> Dict:

        '''
        It receives a Steam ID and returns that user's tier, along with the API request performance and the billing information that goes to the database for cost calculation and daily rate limit.

        return = {
            'tier': int,
            'performance_open_dota': float
            'billing_open_dota' : int
            }
        '''


        account_id = OpenDotaService().steam32_to_steam64(user_id)

        start_api_call = perf_counter()
        requisicao = requests.get(f'https://api.opendota.com/api/players/{account_id}') 
        req = requisicao.json()

        end_api_call = perf_counter()
        performance = round((end_api_call - start_api_call),2)
        tier = req.get('rank_tier')

        if requisicao.status_code not in (500,429,404 ) :
            billing_open_dota = 1
        else:
            billing_open_dota = 0

        
        req_return = {'tier':tier,
                   'performance_open_dota': performance,
                   'billing_open_dota' : billing_open_dota
        }


        return req_return 
    
    

if __name__ == '__main__':
    ranking_id = os.getenv('RANKING_STEAM')
    ranking = ranking_id

    tier = OpenDotaService().tier_request(user_id=ranking)

    print(tier)

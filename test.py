import requests


def steam32_to_steam64( steam_id: str) -> str:
        '''
        recebe uma string que seria o steamid de um usuário, para retornar uma string que seria o user_id requerido pela api do open_dota para que faça as demais buscas

        essa função é usada apenas nas funções para chamada de api do open_dota, e não necessita de uso fora desse escopo
        
        '''

        valor_offset = 76561197960265728

        return str(int(steam_id) - valor_offset)

ranking = '76561198266319437'
account_id = steam32_to_steam64(ranking)

params = {'date': 5}
url = f'https://api.opendota.com/api/players/{account_id}/heroes'

req = requests.get(url=url, params=params)

response = req.json()
response
'''
Still a test to populate the bd.

This part will be in some service to futhermore we can calculate probalilities of wins, or to mount teams within the players.

'''
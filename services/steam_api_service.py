import os
from typing import Dict, List, Any
import requests
from dotenv import load_dotenv
from time import sleep, perf_counter


#carregando as váriaveis de sistema (chaves de api)
load_dotenv()

class SteamApiService:
 
    def __init__(self):

        STEAMKEY = os.getenv('API_STEAM')
        self.steam_key = STEAMKEY

       
    def listar_amigos_raw(self, id_ranking: str) -> Dict:
        '''
        Recebe o id_ranking como string, retorna um dicionáro com a lista de amigos dessa conta, e a informação de performance.

        exemplo de retorno:
            retorno = {
                'amigos': [str], 
                'performance_steam': foat
                }
                
        
        '''
        start_api_call = perf_counter()

        dic_amigos = requests.get(f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={self.steam_key}&steamid={id_ranking}&relationship=friend").json()

        end_api_call = perf_counter()


        #criando a lista de amigos a partir do dicionario da chamada de API o retorno é uma lista de steamid

        lista_amigos = [amigo.get('steamid') for amigo in dic_amigos.get('friendslist').get('friends')]#[0:5]

        performance = round((end_api_call - start_api_call),2)
        
        retorno ={'amigos': lista_amigos,
                  'performance_steam': performance}

        return retorno
        

    def solicitar_dados_amigos(self, amigo: str) -> Dict:
        '''
        Recebe uma string com o ID_steam de um amigo, para que seja solicitado a API da steam os dados desse amigo, e o tempo de performance da solicitação como um dicionário de dicionários.
        exemplo de retorno:
            retorno = {
                        'dados':{
                            'steamid': str,
                            'personaname: str,
                            'communityvisibilitystate: int,
                            'avatarfull': str},
                        'performance_steam': float    
                            }
        
        tendo assim o retorno com duas keys, "dados" que é um dicionário contendo os dados do amigo, e "performance" que é um valor float mostrando o tempo da performance da requisição 

        para acessar os dados basta acessar a chave do dicionario.
        ex:

        print(retorno['dados'])

        >>> {'steamid': '76561197975609491', 'personaname': 'nome', 'profilestate': 1, 'avatarfull': 'https://avatars.steamstatic.com/79a8119bd2a027755f93872d0d09b959909a0405_full.jpg'}


        '''
        start_api_call = perf_counter()
        amigo = requests.get(f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={self.steam_key}&steamids={amigo}").json().get('response').get('players')

    
        dados_amigos = {
            'steamid': amigo[0].get('steamid'),
            'personaname': amigo[0].get('personaname'),
            'communityvisibilitystate': amigo[0].get('communityvisibilitystate'),
            'avatarfull': amigo[0].get('avatarfull')
        }
        
        end_api_call = perf_counter()
        performance = round((end_api_call - start_api_call),2)
        return {'dados':dados_amigos,
                'performance_steam': performance}

            
    


if __name__ == '__main__':
    ranking = "76561198266319437"
    lista_amigos_raw= SteamApiService().listar_amigos_raw(id_ranking=ranking)
    lista_amigos_dados = lista_amigos_raw['amigos']
    print(lista_amigos_dados)


 
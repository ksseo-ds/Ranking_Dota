from dotenv import load_dotenv
from front.front import *
import os
import requests
from time import sleep
#carregando as váriaveis de sistema (chaves de api)
load_dotenv()


class Requisicao:
 
    def __init__(self):

        steamKey = os.getenv('API_STEAM')
        openDotaKey = os.getenv('OPEN_DOTA_API')

        self.steamKey = steamKey
        self.openDotaKey = openDotaKey
        
    
    def atualizar_lista_amigos(self,id_ranking:str) -> list[dict]:    
        '''
        Recebe uma string com o id da steam do ranking para que busque a lista de amigos.

        À partir da lista de amigos, percorre amigo por amigo e atualiza os dados em uma lista de dicionários onde cada amigo é um dicionário.

        [{'steamid', 'personaname', 'profilestate', 'avatarfull'}]


        '''

        dic_amigos = requests.get(f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={self.steamKey}&steamid={id_ranking}&relationship=friend").json()


        #criando a lista de amigos a partir do dicionario da chamada de API o retorno é uma lista de steamid
        lista_amigos = [amigo.get('steamid') for amigo in dic_amigos.get('friendslist').get('friends')]#[0:5]

        #criando uma lista vazia para incluir os dados de cada amigo, que será o retorno da função
        retorno = []
        contador = 0
        #populando a lista "retorno" com os dados dos usuarios que foram colhidos na steamapi
        for amigo in lista_amigos:
            amigo = requests.get(f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={self.steamKey}&steamids={amigo}").json().get('response').get('players')
            contador += 1
            print(f"atualizando {contador} / {len(lista_amigos)} {amigo[0].get('personaname')}")
            dados_atualizaveis = {
                'steamid': amigo[0].get('steamid'),
                'personaname': amigo[0].get('personaname'),
                'profilestate': amigo[0].get('profilestate'),
                'avatarfull': amigo[0].get('avatarfull')
            }
            retorno.append(dados_atualizaveis)
            
        
        return retorno
    

    @staticmethod
    def steam32_to_steam64(steamid:str) -> str:
        '''
        A api do Opendota usa o Account Id, e a steam fornece o steamid32

        pra que consigamos solicitar dados da API precisamos diminuir o steamId32 da conta pelo offset, que é um número fixo
        '''
        valor_offset = 76561197960265728

        return str(int(steamid)- valor_offset)

    @staticmethod
    def requisita_open_dota(id_ranking:str):

        account_id = Requisicao.steam32_to_steam64(id_ranking)

        req = requests.get(f'https://api.opendota.com/api/players/{account_id}').json()
    
        return req.get("rank_tier")

    @staticmethod
    def atualizar_tier(listadeamigos:list[dict]) -> list[dict]:
        contador = 0

        for i,amigo in enumerate(listadeamigos):
            if amigo.get('profilestate') == 1 : # verifica se perfil é público
                try:
                    contador += 1 # Serve apenas para verificar o progresso
                    tier = Requisicao.requisita_open_dota(amigo['steamid']) # solicita o Tier do Open_dota
                    print(f"Atualizando Tier {contador} / {len(listadeamigos)} {amigo['personaname']}") # barra de progresso

                    listadeamigos[i] = {
                        'steamid' :amigo['steamid'],
                        'tier':tier
                    }
                
                    sleep(1)
                    ...
                except: pass
            else : pass
        
        
        return listadeamigos



if __name__=="__main__":

    account_id = Requisicao()
    account_id = account_id.steam32_to_steam64(steamid="76561198266319437")    
        
    #requ = requests.get(f'https://api.opendota.com/api/players/{account_id}')
    lista_de_amigos = [{'steamid': '76561198266319437', 'personaname': 'ZURETAWN', 'profilestate': 1, 'avatarfull': 'https://avatars.steamstatic.com/522c69e28bb361ddb4c93e251942286b3bc7c1a3_full.jpg'}, {'steamid': '76561198217022684', 'personaname': 'LUÍNDIO', 'profilestate': 1, 'avatarfull': 'https://avatars.steamstatic.com/e61b6d6c317eea531b4b6ad3ac79be64ccd4f204_full.jpg'}]
    
    Requisicao.atualizar_tier(listadeamigos=lista_de_amigos)

    lista_de_amigos
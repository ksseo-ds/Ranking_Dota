import os
from typing import Dict 
import requests
from dotenv import load_dotenv
from time import perf_counter


#loading ENV variables
load_dotenv()

class SteamApiService:
 
    def __init__(self):

        STEAMKEY = os.getenv('API_STEAM')
        self.steam_key = STEAMKEY

       
    def raw_friend_list(self, id_ranking: str) -> Dict:
        '''
        It receives the id_ranking as a string, returns a dictionary with the list of friends for that account, and performance information.
        
        return example:
            return = {
                'amigos': [str], 
                'performance_steam': foat
                }
                
        'amigos' => friends 

                
        '''
        start_api_call = perf_counter()

        friends_dict = requests.get(f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={self.steam_key}&steamid={id_ranking}&relationship=friend").json()

        end_api_call = perf_counter()


        #Creating the friends list from the API call dictionary returns a list of Steam IDs.

        friends_list = [amigo.get('steamid') for amigo in friends_dict.get('friendslist').get('friends')]#[0:5]

        performance = round((end_api_call - start_api_call),2)
        
        req_return ={'amigos': friends_list,
                  'performance_steam': performance}

        return req_return
        

    def player_data_request(self, player: str) -> Dict:
        '''
        Receives a string containing a friend's Steam ID, so that the Steam API can be requested to retrieve that friend's data, and the request's performance time is measured as a dictionary of dictionaries.
        Example return:
            return = {
                        'dados':{
                            'steamid': str,
                            'personaname: str,
                            'communityvisibilitystate: int,
                            'avatarfull': str},
                        'performance_steam': float    
                            }
        
        The result is a return with two keys: "dados," which is a dictionary containing the friend's data, and "performance," which is a float value showing the request's performance time.

        To access the data, simply access the dictionary key.

        Example:

        print(retorno['dados'])

        >>> {'steamid': '76561197975609491', 'personaname': 'nome', 'profilestate': 1, 'avatarfull': 'https://avatars.steamstatic.com/79a8119bd2a027755f93872d0d09b959909a0405_full.jpg'}
        '''


        start_api_call = perf_counter()
        player = requests.get(f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={self.steam_key}&steamids={player}").json().get('response').get('players')

    
        player_data = {
            'steamid': player[0].get('steamid'),
            'personaname': player[0].get('personaname'),
            'communityvisibilitystate': player[0].get('communityvisibilitystate'),
            'avatarfull': player[0].get('avatarfull')
        }
        
        end_api_call = perf_counter()
        performance = round((end_api_call - start_api_call),2)

        return {'dados':player_data,
                'performance_steam': performance}

            
    


if __name__ == '__main__':

    ranking_id = os.getenv('RANKING_STEAM')
    ranking = ranking_id
    raw_friend_list= SteamApiService().raw_friend_list(id_ranking=ranking)
    friend_list = raw_friend_list['amigos']
    print(friend_list)


 
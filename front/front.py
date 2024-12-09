import os
class Menu:
    def __init__(self):
        pass


    def menu_inicial(self):
        steam_id_ranking = 0
        os.system('clear')
        print('============XX===========')
        print('Menu: Escolha o Usuário: ')
        print('1 - Usuário teste')
        print('2 - Outro Usuário')
        print('============XX===========')
        escolha = int(input('Um número: '))

        if escolha == 1:
            steam_id_ranking = "76561198266319437"
            os.system('clear')
            escolha = 0
            return steam_id_ranking

        if escolha == 2:
            print('Digite o usuário: ')
            steam_id_ranking = str(input('digite o steam_id'))
            escolha = 0
            return steam_id_ranking
            
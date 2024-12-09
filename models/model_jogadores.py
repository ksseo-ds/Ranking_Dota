from peewee import *
from .db import db_dota 


class Banco(Model):
    class Meta:
        database = db_dota 

class Jogadores(Banco):
    steam_id = CharField(unique=True)
    personaname = CharField()
    profilestate= SmallIntegerField()
    #tier = SmallIntegerField()  # retiramos para fazer apenas a tabela fato, o tier vai ser migrado para outra tabela
    avatar = CharField()
    
    class Meta:
        table_name = "jogadores"

    @staticmethod
    def adicionar_jogador(steam_id, personaname, profilestate, avatar):
        '''
        Sub_rotina que adiciona ou atualiza jogadores no banco de dados, a partir do 'comando adicionar_a_ BD'.

        a diferença é que o comando 'adicionar_ao_BD' recebe uma lista de dicionários com os dados de jogadores, e após verificação se o jogador existe
        ou não é feita uma iteração em cada jogador e 'adicionar_jogador()' é executado no jogador.

        o retorno é o usuário e ja atualiza no BD
        '''    
         
        try:
            usuario = Jogadores.create(
                                steam_id = steam_id,
                                personaname = personaname,
                                profilestate = profilestate,
                                avatar = avatar
                                
                                )
        
            return usuario
    
        except IntegrityError:  # Ocorre se o steam_id já existe no banco
            Jogadores.update(
            personaname=personaname,
            profilestate=profilestate,
            avatar=avatar
            ).where(Jogadores.steam_id == steam_id).execute()
                

    @staticmethod
    def verifica_jogador_novo(jogador) -> bool:
        '''
        Sub Rotina do 'adicionar_ao_bd', verifica se o jogador existe ou não no bd, para que seja encaminhado para a criação ou a atualização.

        recebe o dicionário contendo o jogador, verifica se o 'steam_id' consta no bd, e retorna um booleano se existe ou não
        
        '''
        existe = Jogadores.select().where(Jogadores.steam_id == jogador.get('steam_id')).exists()
        return existe      



    @staticmethod
    def adicionar_ao_bd(lista) -> None :

        '''
        Código para adicionar ao banco de dados à partir uma lista de dicionários.

        Percorre a lista e executa a subrotina 'verifica_jogador_novo(jogador)' iterando em cada dicionário de jogadores e verificando se o jogador Existe no bd
        Caso não exista ele roda o 'adicionar_jogador'

        esse metodo não tem retorno


        p.s: na versão atual ele não verifica se existe ou não, pois o "adicionar_jogador" está fazendo essa verificação, independente de existir ou não
        '''

        for amigo in lista:
            existe = Jogadores.verifica_jogador_novo(amigo)
            
            
            steam_id = amigo.get('steamid') 
            personaname = amigo.get('personaname') 
            profilestate= amigo.get('profilestate') 
            avatar = amigo.get('avatarfull')

            Jogadores.adicionar_jogador(steam_id=steam_id,
                                        personaname=personaname,
                                        profilestate=profilestate, 
                                        avatar=avatar
                                        )
            
            
            


             
            
    





if __name__ == "__main__":

    lista = [{"steamid":"0123","personaname":"cassio", "profilestate":1,"avatarfull":"teste1.jpg", "tier":22},
             {"steamid":"01234","personaname":"cassio2", "profilestate":1,"avatarfull":"teste2.jpg", "tier": 29}]

    usuario = Jogadores()
    db_dota.connect()

    db_dota.create_tables([Jogadores], safe = True)

    Jogadores.adicionar_ao_bd(lista)
    
    db_dota.close()
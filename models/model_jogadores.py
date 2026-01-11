from peewee import Model, CharField, SmallIntegerField, IntegrityError
from models.db import DbDota, db_dota 


class Jogadores(DbDota):
    steam_id = CharField(primary_key=True)
    personaname = CharField()
    profilestate= SmallIntegerField()
    avatar = CharField()
    
    class Meta:
        table_name = "jogadores"

    def __str__(self):
        return self.personaname

    @classmethod
    def adicionar_jogador(cls, steam_id, personaname, profilestate, avatar):
        '''
        Sub_rotina que adiciona ou atualiza jogadores no banco de dados, a partir do 'comando adicionar_a_ BD'.

        a diferença é que o comando 'adicionar_ao_BD' recebe uma lista de dicionários com os dados de jogadores, e após verificação se o jogador existe
        ou não é feita uma iteração em cada jogador e 'adicionar_jogador()' é executado no jogador.

        o retorno é o usuário e ja atualiza no BD
        '''    

        if db_dota.is_closed():
            db_dota.connect()

        else: pass

        try:
            Jogadores.create(
                            steam_id = steam_id,
                            personaname = personaname,
                            profilestate = profilestate,
                            avatar = avatar
                            )
        
            
    
        except IntegrityError:  # Ocorre se o steam_id já existe no banco
            Jogadores.update(
            personaname=personaname,
            profilestate=profilestate,
            avatar=avatar
            ).where(Jogadores.steam_id == steam_id).execute()

        if not db_dota.is_closed():
            db_dota.close()

        
if __name__ == "__main__":
    
    db_dota.connect

    Jogadores().adicionar_jogador(steam_id=123, personaname='testee', profilestate=3, avatar='teste.jpg')

    consulta = Jogadores.select().where(Jogadores.steam_id == 123)

    for jogadores in consulta:
        print(jogadores)

    Jogadores().delete().where(Jogadores.steam_id == 123)

    db_dota.close()
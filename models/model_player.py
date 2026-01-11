from peewee import CharField, SmallIntegerField, IntegrityError
from models.db import DbDota, db_dota 


class Player(DbDota):
    steam_id = CharField(primary_key=True)
    personaname = CharField()
    profilestate= SmallIntegerField()
    avatar = CharField()
    
    class Meta:
        table_name = "jogadores"

    def __str__(self):
        return self.personaname

    @classmethod
    def create_update_player(cls, steam_id, personaname, profilestate, avatar):
        '''
        Subroutine that adds or updates players in the database

        params:
            steam_id : int
            personaname : str
            profilestate : int
            avatar : str

        The return is the user and it updates the database.
        '''    

        if db_dota.is_closed():
            db_dota.connect()

        else: pass

        try:
            Player.create(
                            steam_id = steam_id,
                            personaname = personaname,
                            profilestate = profilestate,
                            avatar = avatar
                            )
        
            
    
        except IntegrityError:  # If this happen it means that the player is persisted Already, it will update instead 
            Player.update(
            personaname=personaname,
            profilestate=profilestate,
            avatar=avatar
            ).where(Player.steam_id == steam_id).execute()

        if not db_dota.is_closed():
            db_dota.close()

        
if __name__ == "__main__":
    
    db_dota.connect

    Player().create_update_player(steam_id=123, personaname='testee', profilestate=3, avatar='teste.jpg')

    consulta = Player.select().where(Player.steam_id == 123)

    for jogadores in consulta:
        print(jogadores)

    Player().delete().where(Player.steam_id == 123)

    db_dota.close()
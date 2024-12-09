from peewee import *
from db import db_dota 
from datetime import datetime


class Banco(Model):
    class Meta:
        database = db_dota 

class Sessao(Banco):
    date = DateTimeField()
    
    class Meta:
        table_name = "sessao"


    @staticmethod
    def gerar_nova_sessao() -> int:
        
        data = datetime.now()
        sessao = Sessao.create(date = data)

        return sessao

if __name__ == "__main__":
    db_dota.connect()

    db_dota.create_tables([Sessao], safe = True)
    
    session = Sessao.gerar_nova_sessao()

    print(session)
    
    db_dota.close()
from peewee import *
from models.db import db_dota 
from datetime import datetime


class Banco(Model):
    class Meta:
        database = db_dota 

class Sessao(Banco):
    date = DateTimeField()
    
    class Meta:
        table_name = "sessao"


    def gerar_nova_sessao() -> int:
        db_dota.connect()
        data = datetime.now()
        sessao = Sessao.create(date = data)
        db_dota.close()
        return sessao

if __name__ == "__main__":
    db_dota.connect()

    db_dota.create_tables([Sessao], safe = True)
    
    session = Sessao.gerar_nova_sessao()

    print(session)
    
    db_dota.close()
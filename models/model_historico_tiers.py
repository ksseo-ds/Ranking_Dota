from peewee import *
from models.db import db_dota
from models.model_jogadores import Jogadores
from models.model_sessao import Sessao
from models.model_tiers import Tiers


class Banco(Model):
    class Meta:
        database = db_dota

class Historico_tier(Banco):
    steam_id = ForeignKeyField(Jogadores, backref='historico', on_delete='CASCADE')
    tier = ForeignKeyField(Tiers, backref='tier', on_delete='CASCADE')
    sessao = ForeignKeyField(Sessao, backref='sessao', on_delete='CASCADE')

    class Meta:
        table_name = 'historico_tier'


    def incluir_tier_bd(jogador:dict) -> None:

        if db_dota.is_closed():
            db_dota.connect()

        else: pass


        if jogador.get('tier') is not None:

            Historico_tier().create(
                tier = jogador['tier'],
                steam_id = jogador['steamid'],
                sessao = jogador['sessao']
            )

        else: pass

        if not db_dota.is_closed():
            db_dota.close()

        

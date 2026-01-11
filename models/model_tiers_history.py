from peewee import ForeignKeyField
from models.db import DbDota,db_dota
from models.model_player import Player
from models.model_session import Sessao
from models.model_tiers import Tiers


class TierHistory(DbDota):
    steam_id = ForeignKeyField(Player, backref='historico', on_delete='CASCADE')
    tier = ForeignKeyField(Tiers, backref='tier', on_delete='CASCADE')
    sessao = ForeignKeyField(Sessao, backref='sessao', on_delete='CASCADE')

    class Meta:
        table_name = 'historico_tier'


    def create_update_tier_db(jogador:dict) -> None:

        if db_dota.is_closed():
            db_dota.connect()

        else: pass


        if jogador.get('tier') is not None:

            TierHistory().create(
                tier = jogador['tier'],
                steam_id = jogador['steamid'],
                sessao = jogador['sessao']
            )

        else: pass

        if not db_dota.is_closed():
            db_dota.close()

        

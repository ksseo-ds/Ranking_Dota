from peewee import *
from .db import db_dota 

#from . import model_jogadores, model_sessao



class Banco(Model):
    class Meta:
        database = db_dota

class Tiers(Banco):
    tier = SmallIntegerField(unique=True, primary_key= True)
    tier_name = CharField()
    tier_star = SmallIntegerField()

    class Meta:
        table_name = "tiers"

    def popular_tabela_tiers():
        lista =[(11, 'Arauto', 1), 
                (12, 'Arauto', 2),
                (13, 'Arauto', 3),
                (14, 'Arauto', 4),
                (15, 'Arauto', 5),
                (21, 'Guardião', 1),
                (22, 'Guardião', 2),
                (23, 'Guardião', 3),
                (24, 'Guardião', 4),
                (25, 'Guardião', 5),
                (31, 'Cruzado', 1),
                (32, 'Cruzado', 2),
                (33, 'Cruzado', 3),
                (34, 'Cruzado', 4),
                (35, 'Cruzado', 5),
                (41, 'Arquimago', 1),
                (42, 'Arquimago', 2),
                (43, 'Arquimago', 3),
                (44, 'Arquimago', 4),
                (45, 'Arquimago', 5),
                (51, 'Lenda', 1),
                (52, 'Lenda', 2),
                (53, 'Lenda', 3),
                (54, 'Lenda', 4),
                (55, 'Lenda', 5),
                (61, 'Ancião', 1),
                (62, 'Ancião', 2),
                (63, 'Ancião', 3),
                (64, 'Ancião', 4),
                (65, 'Ancião', 5),
                (71, 'Divino', 1),
                (72, 'Divino', 2),
                (73, 'Divino', 3),
                (74, 'Divino', 4),
                (75, 'Divino', 5),
                (80, 'Imortal', 0)]

        for tupla in lista:
            try:
                Tiers.create(
                    tier = tupla[0],
                    tier_name = tupla[1],
                    tier_star = tupla[2]
                    )
            except IntegrityError:
                Tiers.update(
                    tier = tupla[0],
                    tier_name = tupla[1],
                    tier_star = tupla[2]
                    )


class Hitorico_Tiers(Banco):

    class Meta:
        table_name = "historico_tiers"




if __name__ == "__main__":
    print('ok')

    db_dota.connect()
    db_dota.create_tables([Tiers], safe = True)

    Tiers.popular_tabela_tiers()

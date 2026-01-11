from peewee import Model, SmallIntegerField, CharField
from db import DbDota, db_dota 


class Tiers(DbDota):
    tier = SmallIntegerField(unique=True, primary_key= True)
    tier_name = CharField()
    tier_star = SmallIntegerField()

    class Meta:
        table_name = "tiers"


    @classmethod
    def pupulate_tier_table(cls):

        if db_dota.is_closed():
            db_dota.connect()
            print('Models/tiers conectando no BD')

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
                (41, 'Arconte', 1),
                (42, 'Arconte', 2),
                (43, 'Arconte', 3),
                (44, 'Arconte', 4),
                (45, 'Arconte', 5),
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
                # Tenta atualizar se o registro já existir
                rows_updated = (
                    Tiers.update(
                        tier_name=tupla[1],
                        tier_star=tupla[2]
                    )
                    .where(Tiers.tier == tupla[0])
                    .execute()
                )
                if rows_updated == 0:  # Se nenhum registro foi atualizado, insere um novo
                    Tiers.create(
                        tier=tupla[0],
                        tier_name=tupla[1],
                        tier_star=tupla[2]
                    )
                    print(f'Created: {tupla}')
                else:
                    print(f'Updated: {tupla}')

            except Exception as e:
                print(f'Processing Error  {tupla}: {e}')

        if not db_dota.is_closed():
            db_dota.close()
            print('Models/tiers Db Disconnecting')


if __name__ == "__main__":
    print('ok')

 

    db_dota.create_tables([Tiers], safe = True)
    Tiers.pupulate_tier_table()

  

    

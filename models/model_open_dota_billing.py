from peewee import Model, IntegerField,ForeignKeyField
from models.model_session import Sessao
from models.db import DbDota, db_dota


class OpenDotaBilling(DbDota):
    session_id = ForeignKeyField(Sessao, backref='sessao', on_delete='CASCADE' )
    requisition_billing = IntegerField()
    
    class Meta:
        table_name = "open_dota_billing"

    @classmethod
    def open_dota_bill(cls, session_id:int, requisition_billing:int) -> None:
        db_dota.connect()
        OpenDotaBilling.create(session_id=session_id, requisition_billing=requisition_billing)
        db_dota.close()

if __name__ == "__main__":
    from models.model_session import Sessao    

    db_dota.create_tables([OpenDotaBilling], safe = True)
    
    try:
        db_dota.close()
    except:
        pass
    session = Sessao.gerar_nova_sessao()
    requisition_billing = 1
    OpenDotaBilling.open_dota_bill(session_id=session, requisition_billing=requisition_billing)

    db_dota.close()

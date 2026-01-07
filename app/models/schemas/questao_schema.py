from app.db_config import ma
from app.models.tables.questao import Questao

class QuestaoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Questao
        load_instance = True

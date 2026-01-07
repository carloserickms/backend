from app.db_config import ma
from app.models.tables.pergunta import Pergunta
from app.models.schemas.questao_schema import QuestaoSchema

class PerguntaSchema(ma.SQLAlchemyAutoSchema):
    questoes = ma.Nested(QuestaoSchema, many=True)
    class Meta:
        model = Pergunta
        load_instance = True

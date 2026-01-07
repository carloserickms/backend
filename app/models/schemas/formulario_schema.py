from app.db_config import ma
from app.models.tables.formulario import Formulario
from app.models.schemas.perguntas_schema import PerguntaSchema

class FormularioSchema(ma.SQLAlchemyAutoSchema):
    perguntas = ma.Nested(PerguntaSchema, many=True)
    class Meta:
        model = Formulario
        load_instance = True

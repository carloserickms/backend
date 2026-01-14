from app.db_config import db
from app.models.tables.pergunta import Pergunta
from app.models.tables.formulario import Formulario
from app.models.tables.questao import Questao
from flask import jsonify, request, Blueprint
from app.models.schemas.formulario_schema import PerguntaSchema

pergunta_route = Blueprint('pergunta_route', __name__)

@pergunta_route.route('/api/v1/criar_pergunta', methods=['POST'])
def criar_pergunta():
    if request.method == 'POST':
        try:
            body = request.get_json()
            titulo = body['titulo']
            formulario_id = body['formulario_id']

            if not titulo:
                return jsonify({"message": "O campo 'titulo' é obrigatório."}), 400
            
            if not formulario_id:
                return jsonify({"message": "O campo 'formulario_id' é obrigatório."}), 400
            
            formulario = Formulario.query.filter_by(id=formulario_id).first()
            if not formulario:
                return jsonify({"message": "Formulario nao encontrado."}), 400
        

            pergunta = Pergunta(formulario_id=formulario_id, titulo=titulo)

            db.session.add(pergunta)
            db.session.commit()

            pergunta_id = Pergunta.query.filter_by(titulo=titulo, formulario_id=formulario_id).first().id

            return jsonify({
                "status": "ok",
                "message": "Pergunta criada com sucesso!",
                "id": pergunta_id
                }), 201
        
        except Exception as error:
            return jsonify({
                    'status': 'error',
                    'message': f'An error has occurred!{str(error)}'
                }), 500
        
@pergunta_route.route('/api/v1/listar_perguntas', methods=['GET'])
def listar_perguntas():
    perguntas = Pergunta.query.all()
    perguntas_schema = PerguntaSchema(many=True)

    return perguntas_schema.dump(perguntas)

@pergunta_route.route('/api/v1/editar_pergunta', methods=['POST'])
def editar_pergunta():
    if request.method == 'POST':
        try:
            body = request.get_json()
            id = body['id']
            titulo = body['titulo']

            if not titulo:
                return jsonify({"message": "O campo 'titulo' é obrigatório."}), 400
            
            pergunta = Pergunta.query.filter_by(id=id).first()
            if not pergunta:
                return jsonify({"message": "Pergunta nao encontrada."}), 400

            pergunta.titulo = titulo

            db.session.commit()
            db.session.close()

            return jsonify({
                "status": "ok",
                "message": "Pergunta editada com sucesso!"
                }), 200
        
        except Exception as error:
            return jsonify({
                    'status': 'error',
                    'message': f'An error has occurred!{str(error)}'
                }), 500
        
@pergunta_route.route('/api/v1/deletar_pergunta', methods=['POST'])
def deletar_pergunta():
    if request.method == 'POST':
        try:
            body = request.get_json()
            id = body['id']

            pergunta = Pergunta.query.filter_by(id=id).first()
            if not pergunta:
                return jsonify({"message": "Pergunta nao encontrada."}), 400

            db.session.delete(pergunta)
            db.session.commit()
            db.session.close()

            return jsonify({
                "status": "ok",
                "message": "Pergunta deletada com sucesso!"
                }), 200
        
        except Exception as error:
            return jsonify({
                    'status': 'error',
                    'message': f'An error has occurred!{str(error)}'
                }), 500
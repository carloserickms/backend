from app.db_config import db
from app.models.tables.questao import Questao
from app.models.tables.pergunta import Pergunta
from app.models.tables.formulario import Formulario
from flask import jsonify, request, Blueprint
from app.models.schemas.questao_schema import QuestaoSchema

questao_route = Blueprint('questao_route', __name__)

@questao_route.route('/api/v1/criar_questao', methods=['POST'])
def criar_questao():
    if request.method == 'POST':
        try:
            body = request.get_json()
            titulo = body['titulo']
            pergunta_id = body['pergunta_id']

            if not titulo:
                return jsonify({"message": "O campo 'titulo' é obrigatório."}), 400
            
            if not pergunta_id:
                return jsonify({"message": "O campo 'pergunta_id' é obrigatório."}), 400
            
            questoes = Questao.query.filter_by(pergunta_id=pergunta_id).all()

            if len(questoes) >= 4:
                return jsonify({"message": "Pergunta possui 4 questões."}), 400

            questao = Questao(pergunta_id=pergunta_id, titulo=titulo)

            db.session.add(questao)
            db.session.commit()
            db.session.close()

            return jsonify({
                "status": "ok",
                "message": "Questão criada com sucesso!"
                }), 201
        
        except Exception as error:
            return jsonify({
                    'status': 'error',
                    'message': f'An error has occurred!{str(error)}'
                }), 500
        
@questao_route.route('/api/v1/responder_questao', methods=['POST'])
def responder_questao():
    try:
        body = request.get_json()
        questao_id = body.get("id")

        if not questao_id:
            return jsonify({"message": "ID da questão é obrigatório."}), 400

        questao = (
            db.session.query(Questao)
            .join(Pergunta, Questao.pergunta_id == Pergunta.id)
            .join(Formulario, Pergunta.formulario_id == Formulario.id)
            .filter(
                Questao.id == questao_id,
                Formulario.ativo.is_(True)
            )
            .first()
        )

        if not questao:
            return jsonify({
                "message": "Questão inválida, não pertence a uma pergunta ou formulário ativo."
            }), 400

        questao.quantidade_respostas += 1
        db.session.commit()

        return jsonify({
            "status": "ok",
            "message": "Resposta registrada com sucesso!"
        }), 200

    except Exception as error:
        db.session.rollback()
        return jsonify({
            "status": "error",
            "message": f"An error has occurred! {str(error)}"
        }), 500
        
@questao_route.route('/api/v1/editar_questao', methods=['POST'])
def editar_questao():
    if request.method == 'POST':
        try:
            body = request.get_json()
            id = body['id']
            titulo = body['titulo']

            if not titulo:
                return jsonify({"message": "O campo 'titulo' é obrigatório."}), 400
            
            questao = Questao.query.filter_by(id=id).first()
            if not questao:
                return jsonify({"message": "Questão não encontrada."}), 400
            
            questao.titulo = titulo

            db.session.commit()
            db.session.close()

            return jsonify({
                "status": "ok",
                "message": "Questão editada com sucesso!"
                }), 200
        
        except Exception as error:
            return jsonify({
                    'status': 'error',
                    'message': f'An error has occurred!{str(error)}'
                }), 500
        
@questao_route.route('/api/v1/deletar_questao', methods=['POST'])
def deletar_questao():
    if request.method == 'POST':
        try:
            body = request.get_json()
            id = body['id']

            questao = Questao.query.filter_by(id=id).first()
            if not questao:
                return jsonify({"message": "Questão não encontrada."}), 400

            db.session.delete(questao)
            db.session.commit()
            db.session.close()

            return jsonify({
                "status": "ok",
                "message": "Questão deletada com sucesso!"
                }), 200
        
        except Exception as error:
            return jsonify({
                    'status': 'error',
                    'message': f'An error has occurred!{str(error)}'
                }), 500
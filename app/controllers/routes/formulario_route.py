from app.db_config import db
from app.models.tables.formulario import Formulario
from app.models.tables.pergunta import Pergunta
from app.models.tables.questao import Questao
from flask import jsonify, request, Blueprint
from app.models.schemas.formulario_schema import FormularioSchema

formulario_route = Blueprint('formulario_route', __name__)

@formulario_route.route('/api/v1/criar_formulario', methods=['POST'])
def criar_formulario():
    if request.method == 'POST':
        try:
            body = request.get_json()
            titulo = body['titulo']

            if not titulo:
                return jsonify({"message": "O campo 'titulo' é obrigatório."}), 400
            
            formulario = Formulario(titulo=titulo, ativo=False)

            db.session.add(formulario)
            db.session.commit()
            db.session.close()

            return jsonify({
                "status": "ok",
                "message": "Formulario criado com sucesso!"
                }), 201
        
        except Exception as error:
            return jsonify({
                    'status': 'error',
                    'message': f'An error has occurred!{str(error)}'
                }), 500
        
@formulario_route.route('/api/v1/exibir_formularios', methods=['GET'])
def exibir_formularios():
    if request.method == 'GET':
        try:
            formularios = Formulario.query.filter_by(ativo=True).all()
            formulario_schema = FormularioSchema(many=True)
            print ("aqui passou")
            formularios_data = formulario_schema.dump(formularios)

            return jsonify({
                "status": "ok",
                "data": formularios_data
                }), 200
        
        except Exception as error:
            return jsonify({
                    'status': 'error',
                    'message': f'An error has occurred!{str(error)}'
                }), 500

@formulario_route.route('/api/v1/exibir_todos_formularios', methods=['GET'])
def exibir_todos_formularios():
    if request.method == 'GET':
        try:
            formularios = Formulario.query.all()
            formulario_schema = FormularioSchema(many=True)
            print ("aqui passou")
            formularios_data = formulario_schema.dump(formularios)

            return jsonify({
                "status": "ok",
                "data": formularios_data
                }), 200
        
        except Exception as error:
            return jsonify({
                    'status': 'error',
                    'message': f'An error has occurred!{str(error)}'
                }), 500

@formulario_route.route('/api/v1/ativar_formulario', methods=['POST'])
def ativar_formulario():
    if request.method == 'POST':
        try:
            body = request.get_json()
            id = body['id']

            formulario = Formulario.query.filter_by(id=id).first()
            if not formulario:
                return jsonify({"message": "Formulario nao encontrado."}), 400
            
            formulario.ativo = True

            db.session.commit()
            db.session.close()

            return jsonify({
                "status": "ok",
                "message": "Formulario ativado com sucesso!"
                }), 201
        
        except Exception as error:
            return jsonify({
                    'status': 'error',
                    'message': f'An error has occurred!{str(error)}'
                }), 500
        
@formulario_route.route('/api/v1/desativar_formulario', methods=['POST'])
def desativar_formulario():
    if request.method == 'POST':
        try:
            body = request.get_json()
            id = body['id']

            formulario = Formulario.query.filter_by(id=id).first()
            if not formulario:
                return jsonify({"message": "Formulario nao encontrado."}), 400
            
            formulario.ativo = False

            db.session.commit()
            db.session.close()

            return jsonify({
                "status": "ok",
                "message": "Formulario desativado com sucesso!"
                }), 201
        
        except Exception as error:
            return jsonify({
                    'status': 'error',
                    'message': f'An error has occurred!{str(error)}'
                }), 500
        
@formulario_route.route('/api/v1/auditar_formulario', methods=['GET'])
def auditar_formulario():
    try:
        body = request.get_json()
        formulario_id = body.get("id")

        if not formulario_id:
            return jsonify({"message": "ID do formulário é obrigatório."}), 400

        formulario = (
            db.session.query(Formulario)
            .filter(Formulario.id == formulario_id)
            .first()
        )

        if not formulario:
            return jsonify({"message": "Formulário ativo não encontrado."}), 404

        perguntas = (
            db.session.query(Pergunta)
            .filter(Pergunta.formulario_id == formulario.id)
            .all()
        )

        resultado = {
            "formulario_id": formulario.id,
            "titulo": getattr(formulario, "titulo", None),
            "perguntas": []
        }

        for pergunta in perguntas:
            questoes = (
                db.session.query(Questao)
                .filter(Questao.pergunta_id == pergunta.id)
                .all()
            )

            respostas_totais = sum(questao.quantidade_respostas for questao in questoes)

            resultado["perguntas"].append({
                "pergunta_id": pergunta.id,
                "titulo": pergunta.titulo,
                "questoes": [
                    {
                        "questao_id": questao.id,
                        "questão": questao.titulo,
                        "quantidade_respostas": questao.quantidade_respostas
                    }
                    for questao in questoes
                ], 
                "respostas_totais": respostas_totais
            })

        return jsonify({
            "status": "ok",
            "data": resultado
        }), 200

    except Exception as error:
        db.session.rollback()
        return jsonify({
            "status": "error",
            "message": f"An error has occurred! {str(error)}"
        }), 500
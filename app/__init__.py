from flask import Flask
from flask_cors import CORS
from .db_config import db, ma, migrate
from dotenv import load_dotenv
import os
from app.controllers.routes.formulario_route import formulario_route
from app.controllers.routes.pergunta_route import pergunta_route
from app.controllers.routes.questao_route import questao_route


load_dotenv()


def create_app():
    app = Flask(__name__)

    CORS(
        app,
        resources={r"/api/*": {"origins": "http://localhost:8080"}},
        supports_credentials=True,
        automatic_options=True
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    app.register_blueprint(formulario_route)
    app.register_blueprint(pergunta_route)
    app.register_blueprint(questao_route)

    return app

# Projeto Flask – API com SQLite, SQLAlchemy, Marshmallow e Migrations

Este projeto utiliza **Flask** como framework principal, **SQLite** como banco local, **SQLAlchemy** como ORM, **Marshmallow** para serialização/validação e **Flask-Migrate** para migrações do banco de dados.

---

## 🚀 Requisitos

- Python 3.10+
- Pip instalado
- Git (opcional)

---

## 📦 Criando um Ambiente Virtual

É recomendado usar uma virtual environment (venv) para isolar as dependências do projeto.

### 🔹 Windows (CMD ou PowerShell)

```bash
python -m venv venv
venv\Scripts\activate

🔹 Linux / WSL / macOS

python3 -m venv venv
source venv/bin/activate

Para desativar o ambiente virtual:

deactivate

📚 Instalando as Dependências

Com o ambiente virtual ativado, execute:

pip install -r requirements.txt

📁 Estrutura Sugerida do Projeto

project/
.
└── todolist-backend
    ├── app
    │   ├── controllers
    │   ├── db_config.py
    │   ├── models
    │   ├── repository
    │   └── services
    ├── estrutura.txt
    ├── instance
    ├── readme.md
    ├── requeriments.txt
    ├── run.py


🗄️ Migrações do Banco de Dados (Flask-Migrate)

Gerar as migrações:

flask db init

Criar uma migração:

flask db migrate -m "initial migration"

Aplicar as migrações ao banco:

flask db upgrade

▶️ Executando o Projeto

Com a venv ativa:

flask run

A API estará disponível em:

http://127.0.0.1:5000/

📌 Documentação Oficial das Dependências

Links diretos para consulta dos pacotes usados no projeto:
🧱 Flask

Framework principal.
https://flask.palletsprojects.com/
🔶 Flask-SQLAlchemy

Integração entre Flask e SQLAlchemy.
https://flask-sqlalchemy.palletsprojects.com/
🧬 SQLAlchemy

ORM completo para Python.
https://docs.sqlalchemy.org/
🔄 Flask-Migrate

Migrações automáticas usando Alembic.
https://flask-migrate.readthedocs.io/
🛠 Alembic

Ferramenta de migração usada pelo SQLAlchemy.
https://alembic.sqlalchemy.org/
📝 Marshmallow

Serialização e validação de dados.
https://marshmallow.readthedocs.io/
🔗 Flask-Marshmallow

Integração do Marshmallow com Flask.
https://flask-marshmallow.readthedocs.io/
🧩 Marshmallow-SQLAlchemy

Schemas baseados em modelos SQLAlchemy.
https://marshmallow-sqlalchemy.readthedocs.io/
🔑 python-dotenv

Carrega variáveis de ambiente do arquivo .env.
https://saurabh-kumar.com/python-dotenv/
🧪 Testando a API (Opcional)

Ferramentas recomendadas para testar endpoints:

    Insomnia → https://insomnia.rest

Postman → https://www.postman.com

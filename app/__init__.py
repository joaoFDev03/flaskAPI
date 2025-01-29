from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Carrega as configurações do arquivo config.py
    
    # Importa e registra os blueprints
    from app.controllers.product_controller import product_bp
    from app.controllers.user_controller import user_bp
    from app.controllers.auth_controller import auth_bp
    app.register_blueprint(product_bp, url_prefix='/products')
    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.config['JWT_SECRET_KEY'] = '123'  # Mudar para algo seguro e único

    jwt.init_app(app)

    # Inicializa o banco de dados
    db.init_app(app)
    return app

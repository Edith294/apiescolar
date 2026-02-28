# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from .config import DevelopmentConfig

db = SQLAlchemy()
jwt = JWTManager()

def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    jwt.init_app(app)
    CORS(app)

    # Swagger UI estará en http://localhost:5000/docs/
    swagger_config = {
        "headers": [],
        "specs": [{"endpoint": "apispec", "route": "/apispec.json"}],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/docs/"
    }
    swagger_template = {
        "info": {
            "title": "API Escolar - ITIC",
            "version": "1.0.0",
            "description": "API REST para gestión escolar con Flask y PostgreSQL"
        },
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "Escribe: Bearer <tu_token>"
            }
        }
    }
    Swagger(app, config=swagger_config, template=swagger_template)

    # Registrar blueprints (grupos de rutas)
    from .routes import main_bp
    from .routes.estudiantes import estudiantes_bp
    from .routes.calificaciones import cal_bp
    from .routes.auth import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(estudiantes_bp)
    app.register_blueprint(cal_bp)
    app.register_blueprint(auth_bp)

    return app

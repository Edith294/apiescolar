# app/routes/auth.py
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import db
from app.models.usuario import Usuario
from datetime import timedelta

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth_bp.route("/registro", methods=["POST"])
def registro():
    """
    Registra un nuevo usuario
    ---
    tags:
      - Autenticación
    parameters:
      - in: body
        name: body
        required: true
        schema:
          properties:
            username: {type: string, example: "profe_juan"}
            email: {type: string, example: "juan@uni.edu.mx"}
            password: {type: string, example: "MiPassword123"}
            rol: {type: string, example: "docente"}
    responses:
      201:
        description: Usuario creado
      409:
        description: Username ya en uso
    """
    datos = request.get_json()

    if Usuario.query.filter_by(username=datos.get("username")).first():
        return jsonify({"error": "El username ya está en uso"}), 409

    usuario = Usuario(
        username=datos["username"],
        email=datos["email"],
        rol=datos.get("rol", "docente")
    )
    usuario.set_password(datos["password"])

    db.session.add(usuario)
    db.session.commit()
    return jsonify({"mensaje": "Usuario creado", "id": usuario.id}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    """
    Inicia sesión y devuelve un token JWT
    ---
    tags:
      - Autenticación
    parameters:
      - in: body
        name: body
        required: true
        schema:
          properties:
            username: {type: string, example: "profe_juan"}
            password: {type: string, example: "MiPassword123"}
    responses:
      200:
        description: Token JWT generado
      401:
        description: Credenciales inválidas
    """
    datos = request.get_json()
    usuario = Usuario.query.filter_by(username=datos.get("username")).first()

    if not usuario or not usuario.check_password(datos.get("password", "")):
        return jsonify({"error": "Credenciales inválidas"}), 401

    token = create_access_token(
        identity={"id": usuario.id, "rol": usuario.rol},
        expires_delta=timedelta(hours=24)
    )

    return jsonify({
        "token": token,
        "tipo": "Bearer",
        "expira_en": "24 horas",
        "usuario": {
            "id": usuario.id,
            "username": usuario.username,
            "rol": usuario.rol
        }
    }), 200


@auth_bp.route("/perfil", methods=["GET"])
@jwt_required()
def perfil():
    """
    Obtiene el perfil del usuario autenticado (requiere token JWT)
    ---
    tags:
      - Autenticación
    security:
      - Bearer: []
    responses:
      200:
        description: Perfil del usuario
      401:
        description: Token inválido o expirado
    """
    identidad = get_jwt_identity()
    usuario = Usuario.query.get(identidad["id"])
    return jsonify({
        "usuario": usuario.username,
        "email": usuario.email,
        "rol": identidad["rol"]
    }), 200

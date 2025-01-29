from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.services.user_service import UserService

user_bp = Blueprint('user', __name__)

# Serviço para a lógica do utilizador
user_service = UserService()

# Rota para registar utilizador
@user_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    try:
        user = user_service.register_user(data)
        return jsonify(user), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
# @user_bp.route('/login', methods=['POST'])
# def login_user():
#     data = request.get_json()
#     try:
#         user = user_service.login_user(data)
#         return jsonify(user), 200
#     except ValueError as e:
#         return jsonify({"error": str(e)}), 400

# Rota para listar utilizadores
@user_bp.route('/', methods=['GET'])
def get_users():
    users = user_service.get_all_users()
    return jsonify(users)

# Rota para obter detalhes de um utilizador
@user_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    current_user = get_jwt_identity()
    if user_id:
        try:
            # Converte user_id para inteiro, se possível
            user_id = int(user_id)
            user = user_service.get_user_by_id(user_id)
            if user:
                return jsonify(user,current_user)
        except ValueError:
            # Retorna erro caso user_id não seja um número válido
            return error_response("Invalid user_id. It must be an integer.", 400)
    return error_response("User not found",404)
@user_bp.route('/', methods=['GET'])

def get_user_by_email(email):
    email = request.args.get('email')
    if email:
        user = user_service.get_user_by_email(email)
        if user:
            return jsonify(user)
    return error_response("User not found",404)

@user_bp.route('<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = user_service.delete_user(user_id)
    if user:
        return jsonify(user)
    return error_response("User not found",404)


def error_response(message,status_code):
    return jsonify({"error": message}), status_code
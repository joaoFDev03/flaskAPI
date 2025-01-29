from flask import Blueprint, request, jsonify
from app.services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)
auth_service = AuthService()

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        token = auth_service.login(data)
        return jsonify({"access_token": token}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 401
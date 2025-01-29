

 #Funções de suporte

from flask_jwt_extended import jwt_required, get_jwt_identity

def get_current_user():
    """
    Helper para obter o utilizador atual a partir do token JWT.
    """
    user_identity = get_jwt_identity()
    return user_identity
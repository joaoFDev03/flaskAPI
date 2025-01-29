from marshmallow import ValidationError
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from app.repositories.user_repository import UserRepository
from app.models.user import User
from app import db
from app.schemas.schemas import UserSchema

class AuthService:
    def __init__(self):
        self.user_repo = UserRepository(User,db)

    def login(self, data):
        schema = UserSchema()
        try:
            validated_data = schema.load(data)
        except ValidationError as err:
            raise ValueError(f"Validation Error: {err.messages}")

        # Busca o utilizador pelo email
        user = self.user_repo.get_user_by_email(validated_data["email"])
        
        # Gerar token JWT
        return create_access_token(identity=str(user.id),additional_claims={"email": user.email})

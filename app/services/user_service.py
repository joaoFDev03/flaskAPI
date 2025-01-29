 # Lógica de negócio User
from marshmallow import ValidationError
from app.repositories.user_repository import UserRepository
from app.models.user import User
from app import db
from app.schemas.schemas import UserSchema
class UserService:
    def __init__(self):
        self.user_repo = UserRepository(User,db)
    def register_user(self, data):
        # Verifica se os dados estão corretos
        if not data.get('username') or not data.get('password') or not data.get('email'):
            raise ValueError("Username and password are required")
        
        # Chama o repositório para criar o utilizador
        return self.user_repo.create_user(data)

    def get_all_users(self):
        # Obtém todos os utilizadores
        return self.user_repo.get_all_users()

    def get_user_by_id(self, user_id):
        # Obtém detalhes de um utilizador pelo ID
        return self.user_repo.get_user_by_id(user_id)
    def get_user_by_email(self, email):
        # Obtém detalhes de um utilizador pelo email
        return self.user_repo.get_user_by_email(email)
    def delete_user(self, user_id):
        # Apaga um utilizador pelo ID
        return self.user_repo.delete_user(user_id)

    def login_user(self, data):
    # Valida os dados usando o Marshmallow
        schema = UserSchema()
        try:
            validated_data = schema.load(data)
        except ValidationError as err:
            raise ValueError(f"Validation Error: {err.messages}")

        # Busca o utilizador pelo email
        user = self.user_repo.get_user_by_email(validated_data["email"])
        if not user or user.password != validated_data["password"]:
            raise ValueError("Invalid credentials")

        # Retorna os dados do utilizador autenticado
        return {"message": "User authenticated successfully", "data": {"username": user.username, "email": user.email}}
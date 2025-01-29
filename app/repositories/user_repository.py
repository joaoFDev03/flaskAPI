# Interação com a base de dados
from app.models.user import User
from app import db
from sqlalchemy.exc import IntegrityError

class UserRepository:
    def __init__(self, user_model: User, db_session):
        self.user_model = user_model
        self.db_session = db_session
        
    def create_user(self, data):
        try:
            new_user = self.user_model(username=data['username'], password=data['password'], email=data['email'])
            self.db_session.session.add(new_user)
            self.db_session.session.commit()
            return {"message":"User created successfully","data":{ "id": new_user.id, "username": new_user.username, "email": new_user.email}}
        except IntegrityError as e:
            self.db_session.session.rollback()
            raise ValueError("Email already exists or other integrity error occurred.")
    
    def get_all_users(self):
        # Retorna todos os utilizadores
        return [{"id": user.id, "username": user.username} for user in self.user_model.query.all()]

    def get_user_by_id(self, user_id):
        # Busca um utilizador pelo ID
        user = self.user_model.query.filter_by(id=user_id).first()
        if not user:
            return {"message": "User not found"}
        return {"id": user.id, "username": user.username}
    
    def get_user_by_email(self, email):
        # Busca um utilizador pelo email
        user = self.user_model.query.filter_by(email=email).first()
        if not user:
            return {"message": f"User with email {email} not found"}
        return user
    
    def delete_user(self, user_id):
        # Apaga um utilizador pelo ID
        user = self.user_model.query.filter_by(id=user_id).first() 
        if not user:
            return {"message": "User not found"}
        self.user_model.query.filter_by(id=user_id).delete()
        self.db_session.session.commit()
        return {"message": f"User named {user.username} has been deleted"}
    
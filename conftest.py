import pytest
from app import create_app, db
from app.models.user import User

@pytest.fixture(scope='module')
def test_client():
    # Configurar a aplicação Flask para testes
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Usar banco de dados em memória para testes

    # Criar um cliente de teste
    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()  # Criar o banco de dados e tabelas
            yield testing_client  # Fornecer o cliente de teste para os testes
            db.drop_all()  # Limpar o banco de dados após os testes
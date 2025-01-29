import pytest
from app.models.user import User
from app import db

def test_create_user(test_client):
    # Testar a criação de um usuário
    data = {
        "username": "testuser",
        "password": "testpassword",
        "email": "test@example.com"
    }
    response = test_client.post('/register', json=data)
    assert response.status_code == 201
    assert "id" in response.json
    assert response.json["username"] == "testuser"
    assert response.json["email"] == "test@example.com"

def test_get_user_by_id(test_client):
    # Criar um usuário para testar a busca por ID
    user = User(username="testuser", password="testpassword", email="test@example.com")
    db.session.add(user)
    db.session.commit()

    # Testar a busca por ID
    response = test_client.get(f'/users/{user.id}')
    assert response.status_code == 200
    assert response.json["id"] == user.id
    assert response.json["username"] == "testuser"

def test_get_user_by_email(test_client):
    # Criar um usuário para testar a busca por email
    user = User(username="testuser", password="testpassword", email="test@example.com")
    db.session.add(user)
    db.session.commit()

    # Testar a busca por email
    response = test_client.get(f'/users/email/{user.email}')
    assert response.status_code == 200
    assert response.json["id"] == user.id
    assert response.json["username"] == "testuser"

def test_delete_user(test_client):
    # Criar um usuário para testar a exclusão
    user = User(username="testuser", password="testpassword", email="test@example.com")
    db.session.add(user)
    db.session.commit()

    # Testar a exclusão
    response = test_client.delete(f'/users/{user.id}')
    assert response.status_code == 200
    assert response.status_code == 404
    assert "message" in response.json

def test_login_user(test_client):
    # Criar um usuário para testar o login
    user = User(username="testuser", password="testpassword", email="test@example.com")
    db.session.add(user)
    db.session.commit()

    # Testar o login
    data = {
        "email": "test@example.com",
        "password": "testpassword"
    }
    response = test_client.post('/users/login', json=data)
    assert response.status_code == 200
    assert "id" in response.json
    assert response.json["username"] == "testuser"
    assert response.json["email"] == "test@example.com"
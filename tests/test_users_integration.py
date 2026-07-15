import pytest
from sqlalchemy.exc import IntegrityError

from app.crud import create_user
from app.models import User
from app.schemas import UserCreate


@pytest.mark.integration
def test_create_user_persists_hashed_password(test_db_session):
    user_in = UserCreate(username="jordan", email="jordan@example.com", password="strongpass123")
    user = create_user(test_db_session, user_in)

    assert user.id is not None
    assert user.password_hash != user_in.password
    assert user.username == "jordan"
    assert user.email == "jordan@example.com"

    stored_user = test_db_session.get(User, user.id)
    assert stored_user is not None
    assert stored_user.password_hash == user.password_hash


def test_username_and_email_must_be_unique(test_db_session):
    first_user = User(username="sam", email="sam@example.com", password_hash="hash1")
    test_db_session.add(first_user)
    test_db_session.commit()

    duplicate = User(username="sam", email="other@example.com", password_hash="hash2")
    test_db_session.add(duplicate)
    with pytest.raises(IntegrityError):
        test_db_session.commit()
    test_db_session.rollback()

    duplicate_email = User(username="sam2", email="sam@example.com", password_hash="hash3")
    test_db_session.add(duplicate_email)
    with pytest.raises(IntegrityError):
        test_db_session.commit()
    test_db_session.rollback()


def test_api_rejects_invalid_email(client):
    response = client.post(
        "/users",
        json={"username": "bademail", "email": "bad-email", "password": "strongpass123"},
    )

    assert response.status_code == 422


def test_api_creates_user(client):
    response = client.post(
        "/users",
        json={"username": "newuser", "email": "newuser@example.com", "password": "strongpass123"},
    )

    assert response.status_code == 201
    payload = response.json()
    assert payload["username"] == "newuser"
    assert payload["email"] == "newuser@example.com"
    assert "password_hash" not in payload

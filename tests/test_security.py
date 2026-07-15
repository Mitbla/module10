from app.security import hash_password, verify_password


def test_hash_password_and_verify_password():
    plain_password = "supersecret123"
    password_hash = hash_password(plain_password)

    assert password_hash != plain_password
    assert verify_password(plain_password, password_hash) is True
    assert verify_password("wrongpassword", password_hash) is False

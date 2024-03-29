import pytest # type: ignore
from flask import g, session # type: ignore

from app.db import get_db


def test_register(client, app):
    assert client.get("/auth/register").status_code == 200
    response = client.post("/auth/register", data={"username": "a", "password": "a", "password2": "a"})
    assert response.headers["location"] == "/auth/login"

    with app.app_context():
        assert (
            get_db()
            .execute(
                "select * from user where username = 'a'",
            )
            .fetchone()
            is not None
        )


@pytest.mark.parametrize(
    ("username", "password", "password2", "message"),
    (
        ("", "", "", b"username is required."),
        ("a", "", "", b"password is required."),
        ("test", "test", "test", b"already registered"),
        ("thun", "blue", "blor", b"password does not match")
    ),
)
def test_register_validate_input(client, username, password, password2, message):
    response = client.post(
        "/auth/register", data={"username": username, "password": password,"password2": password2}
    )
    assert message in response.data


def test_login(client, auth):
    assert client.get("/auth/login").status_code == 200
    response = auth.login()
    assert response.headers["Location"] == "/"

    with client:
        client.get("/")
        assert session["user_id"] == 1
        assert g.user["username"] == "test"


@pytest.mark.parametrize(
    ("username", "password", "message"),
    (
        ("a", "test", b"Incorrect username."),
        ("test", "a", b"Incorrect password."),
    ),
)
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data


def test_logout(client, auth):
    auth.login()
    with client:
        auth.logout()
        assert "user_id" not in session

import pytest # type: ignore
from flask import g, session



def test_index(client, auth):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Login" in response.data
    assert b"Register" in response.data
    assert b"Posts" in response.data
    assert b"Vibing" in response.data
    assert b"Meditation" in response.data
    assert b"Todo" in response.data

    auth.login()
    with client:
        response = client.get("/")
        assert b"Logout" in response.data
        assert b"Register" not in response.data
        assert g.user["username"] == "test"
        assert session["user_id"] == 1


@pytest.mark.parametrize("path", ("/todo/", "/posts/"))
def test_login_required(client, path, auth):
    response = client.get(path)
    assert response.headers["Location"] == "/auth/login"
    auth.login()
    with client:
        response = client.get(path)
        assert response.status_code == 200



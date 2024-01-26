def test_todo_index(client, auth):
    auth.login()
    response = client.get("/todo/")
    for i in range(5):
        title = f"test todo {i}".encode("utf-8")
        assert title in response.data

    auth.login("other", "other")
    response = client.get("/todo/")
    for i in range(5, 10):
        title = f"test todo {i}".encode("utf-8")
        assert title in response.data


def test_todo_create(client, auth):
    auth.login()
    response = client.post(
        "/todo/add", data={"title": "create todo", "body": "body of the new things"}
    )
    assert response.headers["Location"] == "/todo/"

    response = client.get("/todo/")
    assert b"create todo" in response.data


def test_todo_delete(client, auth):
    auth.login()
    response = client.post("/todo/delete/1")
    assert response.headers["Location"] == "/todo/"
    assert b"test todo 0" not in client.get("/todo/").data


def test_todo_mark(client, auth):
    auth.login()
    response = client.post("/todo/mark/1")
    assert response.headers["Location"] == "/todo/"
    assert (
        b'<span style="text-decoration: line-through;">test todo 0</span>'
        in client.get("/todo/").data
    )

    response = client.post("/todo/mark/1")
    assert response.headers["Location"] == "/todo/"
    assert b"test todo 0" in client.get("/todo/").data

    response = client.post("/todo/mark/20")
    assert response.headers["Location"] == "/todo/"
    assert b"Todo not found" in client.get("/todo/").data


def test_todo_page(client, auth):
    auth.login()
    reposne = client.get("/todo/1")
    assert b"test todo 0" in reposne.data

    respone = client.get("/todo/20")
    assert respone.headers["Location"] == "/todo/"


def test_edit_todo(client, auth):
    auth.login()
    response = client.post(
        "/todo/edit/1", data={"title": "create todo", "body": "body of the new things"}
    )
    assert response.headers["Location"] == "/todo/1"
    assert b"create todo" in client.get("/todo/1").data

    response = client.post("/todo/edit/20")
    assert response.headers["Location"] == "/todo/"
    assert b"Todo not found" in client.get("/todo/").data
    

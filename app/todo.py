from flask import Blueprint, redirect, render_template, request, session, url_for  # type: ignore

from .auth import login_required
from .db import get_db

bp = Blueprint("todo", __name__, url_prefix="/todo")


@bp.route("/")
@login_required
def index():
    user_id = session["user_id"]
    print(user_id)
    db = get_db()
    todos = db.execute("select * from todo where author_id = ?", (user_id,)).fetchall()
    print([dict(todo) for todo in todos])
    return render_template('todo/index.html', todos=todos)


@bp.post("/add")
def add():
    user_id = session["user_id"]
    title = request.form["title"]
    body = request.form["body"]
    db = get_db()
    db.execute(
        "INSERT INTO todo (title, body, author_id) VALUES(?, ?, ?)",
        (title, body, user_id),
    )
    db.commit()
    return redirect(url_for('todo.index'))



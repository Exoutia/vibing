from flask import Blueprint, flash, g, render_template, redirect, request, url_for  # type: ignore

from .auth import login, login_required
from .db import get_db

bp = Blueprint("todo", __name__, url_prefix="/todo")


@bp.route("/")
@login_required
def index():
    user_id = g.user["id"]
    db = get_db()
    todos = db.execute("select * from todo where author_id = ?", (user_id,)).fetchall()
    print([dict(todo) for todo in todos])
    return render_template("todo/index.html", todos=todos)


@bp.post("/add")
@login_required
def add():
    user_id = g.user["id"]
    title = request.form["title"]
    body = request.form["body"]
    db = get_db()
    db.execute(
        "INSERT INTO todo (title, body, author_id) VALUES(?, ?, ?)",
        (title, body, user_id),
    )
    db.commit()
    return redirect(url_for("todo.index"))


@bp.route("/delete/<int:id>", methods=["POST"])
@login_required
def delete(id):
    db = get_db()
    db.execute("DELETE FROM todo WHERE id = ?", (id,))
    db.commit()
    return redirect(url_for("todo.index"))


@bp.route("/mark/<int:id>", methods=["GET", "POST"])
@login_required
def mark(id):
    db = get_db()
    status = db.execute("SELECT mark FROM todo WHERE id = ?", (id,)).fetchone()
    if status is None:
        flash("Todo not found")
        return redirect(url_for("todo.index"))
    status = not status["mark"]

    db.execute(
        "UPDATE todo SET mark = ? where id = ?",
        (
            status,
            id,
        ),
    )
    db.commit()
    return redirect(url_for("todo.index"))


@bp.route("/<int:id>")
@login_required
def todo_page(id):
    db = get_db()
    todo = db.execute("SELECT * FROM todo WHERE id = ?", (id,)).fetchone()
    if todo is None:
        flash("No todo found with this index.")
        return redirect(url_for("todo.index"))
    print(todo)
    return render_template("todo/todo_page.html", todo=dict(todo))


@bp.route("/edit/<int:id>", methods=["POST"])
@login_required
def edit(id):
    db = get_db()
    todo = db.execute("SELECT * FROM todo WHERE id = ?", (id,)).fetchone()
    if todo is None:
        flash("Todo not found")
        return redirect(url_for("todo.index"))

    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        db.execute(
            "UPDATE todo SET title = ?, body = ? where id = ?",
            (
                title,
                body,
                id,
            ),
        )
        db.commit()
        flash("done editing")
    return redirect(url_for("todo.todo_page", id=id))

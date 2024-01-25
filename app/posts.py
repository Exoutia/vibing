from flask import redirect  # type: ignore
from flask import Blueprint, flash, g, render_template, request, url_for

from app.db import get_db

from .auth import login_required

bp = Blueprint("posts", __name__, url_prefix="/posts")


@bp.route("/")
@login_required
def index():
    db = get_db()
    posts = db.execute(
        """SELECT p.id, u.id as uid, username, p.created_at, title, body FROM post p JOIN user u ON p.author_id = u.id"""
    ).fetchall()
    print([dict(post) for post in posts])
    return render_template("posts/index.html", posts=posts)


@bp.route("/add", methods=["get", "post"])
@login_required
def add():
    if request.method == "POST":
        db = get_db()
        user_id = g.user["id"]
        title = request.form["title"]
        body = request.form["body"]
        db.execute(
            "INSERT INTO post (title, body, author_id) VALUES(?, ?, ?)",
            (title, body, user_id),
        )
        db.commit()
    return redirect(url_for("posts.index"))


@bp.route("/delete/<int:id>", methods=["post"])
@login_required
def delete(id):
    if request.method == "POST":
        db = get_db()
        post = db.execute(
            "SELECT * FROM post WHERE id = ? AND author_id = ?", (id, g.user["id"])
        ).fetchone()
        if post is None:
            flash("You can't delete this post")
        else:
            db.execute("DELETE FROM post WHERE id = ?", (id,))
            db.commit()
            flash("Post deleted successfully")
    return redirect(url_for("posts.index"))


@bp.route("/edit/<int:id>", methods=["get", "post"])
@login_required
def update(id):
    db = get_db()
    post = db.execute(
        "SELECT * FROM post WHERE author_id = ? AND id = ?", (g.user["id"], id)
    ).fetchone()

    if post is None:
        flash("You can't edit this post")
        return redirect(url_for("posts.index"))

    if request.method == "POST" and post is not None:
        title = request.form["title"]
        body = request.form["body"]
        db.execute(
            "UPDATE post SET title = ?, body = ? WHERE id = ?",
            (title, body, id),
        )
        db.commit()
        return redirect(url_for("posts.index"))
    return render_template("posts/edit.html", post=post)

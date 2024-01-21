from flask import Blueprint  # type: ignore
from .auth import login_required

bp = Blueprint("posts", __name__, url_prefix="/posts")


@bp.route("/")
@login_required
def index():
    return "Posts index page"

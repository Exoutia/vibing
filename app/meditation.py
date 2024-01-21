from flask import Blueprint # type: ignore

bp = Blueprint("meditation", __name__, url_prefix="/meditation")

@bp.route("/")
def index():
    return "Meditation index page"

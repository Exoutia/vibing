from flask import Blueprint # type: ignore
from .auth import login_required

bp = Blueprint('todo', __name__, url_prefix='/todo')


@bp.route('/')
@login_required
def index():
    return 'TODO for myself.'

@bp.route('/add', methods=('GET', 'POST'))
def add():
    return 'TODO for the user.'

@bp.route('/delete/<int:id>', methods=('POST', 'GET'))
def delete(id):
    return f'TODO to delete {id}'

@bp.route('/update/<int:id>', methods=('POST', 'GET'))
def update(id):
    return f'TODO to update {id}'

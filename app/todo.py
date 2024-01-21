from flask import Blueprint # type: ignore

bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/')
def index():
    return 'TODO for myself.'

@bp.route('/add', methods=('GET', 'POST'))
def add():
    return 'TODO for the user.'

@bp.delete('/delete/<int:id>', method=('POST', 'GET'))
def delete(id):
    return f'TODO to delete {id}'

@bp.put('/update/<int:id>', method=('POST', 'GET'))
def update(id):
    return f'TODO to update {id}'

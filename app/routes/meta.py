from flask import Blueprint

bp = Blueprint('meta', 'meta')

@bp.route('/')
def index():
    return "hi there"
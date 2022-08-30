from flask import Blueprint, render_template

bp = Blueprint('main', 'main')


@bp.route('/')
def index():
    return render_template('main/index.html')

from io import BytesIO
from base64 import b64encode

from qrcode import make as qrcode_make
from flask import Blueprint, render_template, url_for
from flask_login import login_required

from app.models import Entry
from app.factory import db

bp = Blueprint('raffle', 'raffle')

@bp.route('/enter')
@login_required
def enter_raffle():
    entry = Entry()
    db.session.add(entry)
    db.session.commit()
    _qr = BytesIO()
    qr = qrcode_make(url_for('raffle.show_entry', uuid=entry.uuid, _external=True)).save(_qr)
    return render_template(
        'raffle/enter.html',
        entry=entry,
        qrcode=b64encode(_qr.getvalue()).decode()
    )


@bp.route('/add/prize')
@login_required
def add_prize():
    return 'ok'


@bp.route('/add/drawing')
@login_required
def add_drawing():
    return 'ok'


@bp.route('/show/entry/<uuid>')
def show_entry(uuid):
    entry = Entry.query.filter(Entry.uuid == uuid).first()
    if not entry:
        return redirect(url_for('main.index'))
    if not entry.confirmed:
        entry.confirmed = True
        db.session.commit()
    return render_template(
        'raffle/show_entry.html',
        entry=entry
    )


@bp.route('/show/prize')
def show_prize():
    return 'ok'


@bp.route('/show/drawing')
def show_drawing():
    return 'ok'
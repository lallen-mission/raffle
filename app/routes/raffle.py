from io import BytesIO
from base64 import b64encode

from qrcode import make as qrcode_make
from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_required

from app.models import Entry, Prize
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


@bp.route('/prize/manage', methods=['GET', 'POST'])
@login_required
def manage_prizes():
    if request.method == 'POST' and request.form:
        try:
            assert len(request.form.get('name')) > 3
            existing = Prize.query.filter(Prize.name == request.form.get('name')).first()
            if not existing:
                p = Prize(
                    name=request.form.get('name'),
                    image_url=request.form.get('image_url'),
                    description=request.form.get('description', '')
                )
                db.session.add(p)
                db.session.commit()
                flash('Added new prize!', 'is-success')
            else:
                flash('Prize already exists!', 'is-warning')
        except AssertionError:
            flash('Invalid prize configuration. Try again.', 'is-warning')
        except Exception as e:
            print(e)
            flash('Something went wrong. Try again.', 'is-danger')
    prizes = Prize.query.all()
    return render_template(
        'raffle/manage_prizes.html',
        prizes=prizes
    )


@bp.route('/prize/show/<id>', methods=['GET', 'POST'])
@login_required
def show_prize(id):
    prize = Prize.query.filter(Prize.id == id).first()
    if not prize:
        flash('No prize there big dawg', 'is-warning')
        return redirect(url_for('raffle.manage_prizes'))
    else:
        edited = None
        if request.method == 'POST' and request.form:
            if request.form.get('name') != prize.name:
                prize.name = request.form.get('name')
                db.session.commit()
                edited = True
            if request.form.get('image_url') != prize.image_url:
                prize.image_url = request.form.get('image_url')
                db.session.commit()
                edited = True
            if request.form.get('description') != prize.description:
                prize.description = request.form.get('description')
                db.session.commit()
                edited = True
            if request.form.get('ship') == 'no' and prize.ship_to_winner != False:
                prize.ship_to_winner = False
                db.session.commit()
                edited = True
            elif request.form.get('ship') == 'yes' and prize.ship_to_winner != True:
                prize.ship_to_winner = True
                db.session.commit()
                edited = True
            if edited:
                flash('Edited item!', 'is-success')
            else:
                flash('No changes.', 'is-info')
        return render_template('raffle/show_prize.html', prize=prize)


@bp.route('/prize/delete/<id>')
@login_required
def delete_prize(id):
    prize = Prize.query.filter(Prize.id == id).first()
    if prize:
        flash(f'You deleted prize #{prize.id} ({prize.name})', 'is-success')
        db.session.delete(prize)
        db.session.commit()
        return redirect(url_for('raffle.manage_prizes'))


@bp.route('/drawing/manage')
@login_required
def manage_drawings():
    return render_template('raffle/manage_drawings.html')


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


@bp.route('/show/drawing')
def show_drawing():
    return 'ok'
from uuid import uuid4
from datetime import datetime

from flask import url_for
from flask_login import login_user
from sqlalchemy import inspect

from app.factory import db
from app import config


def rand_id():
    return uuid4().hex

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    register_date = db.Column(db.DateTime, default=datetime.utcnow)
    last_login_date = db.Column(db.DateTime, nullable=True)
    verified = db.Column(db.Boolean, default=False)

    def as_dict(self):
        return {c.key: getattr(self, c.key)
            for c in inspect(self).mapper.column_attrs if c.key != 'nonce'}

    def __repr__(self):
        return str(self.id)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def is_moderator(self):
        return self.moderator

    def get_id(self):
        return self.id

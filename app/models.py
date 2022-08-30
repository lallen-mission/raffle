from uuid import uuid4
from datetime import datetime

from flask_login import login_user
from sqlalchemy import inspect

from app.factory import db


def rand_id():
    return uuid4().hex


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(50), primary_key=True)
    register_date = db.Column(db.DateTime, default=datetime.utcnow)
    last_login_date = db.Column(db.DateTime, nullable=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True, nullable=False)
    profile_pic = db.Column(db.String(150))

    def as_dict(self):
        return {
            c.key: getattr(self, c.key)
            for c in inspect(self).mapper.column_attrs if c.key != 'nonce'
        }

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

    def get_id(self):
        return self.id

    def login(self):
        self.last_login_date = datetime.utcnow()
        login_user(self)
        db.session.commit()

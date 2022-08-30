from logging.config import dictConfig

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mobility import Mobility

from app import config


db = SQLAlchemy()


def setup_db(app: Flask, db: SQLAlchemy = db):
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{config.DB_USER}:{config.DB_PASS}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}' # noqa
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return db


def create_app():
    app = Flask(__name__)
    app.config.from_envvar('FLASK_SECRETS')
    setup_db(app)
    Mobility(app)
    login_manager = LoginManager(app)
    login_manager.login_view = 'meta.index'
    login_manager.logout_view = 'meta.disconnect'

    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        user = User.query.get(user_id)
        return user

    with app.app_context():
        from app.routes import meta
        app.register_blueprint(meta.bp)
        return app
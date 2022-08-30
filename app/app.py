from logging.config import dictConfig

from app.factory import create_app
from app import config


app = create_app()

dictConfig(config.LOGGING_CONFIG)

if __name__ == '__main__':
    app.run()

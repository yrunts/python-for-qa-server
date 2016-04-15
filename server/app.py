
from flask import Flask

from server.security import security_bp, auth_token_required
from server import models


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.default')

    app.register_blueprint(security_bp)

    app.add_url_rule('/', 'index', _index)
    app.add_url_rule('/data', 'data', _data)

    models.init_users()

    return app


def _index():
    return 'Python for QA'


@auth_token_required
def _data():
    return ''

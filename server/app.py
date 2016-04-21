
from flask import Flask
from flask import current_app, abort, request, render_template, make_response

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
    if current_app.user.name != 'admin':
        abort(401, 'admin required')

    match = request.accept_mimetypes.best_match(['application/json',
                                                'application/xml'])
    template = 'test.xml' if match == 'application/xml' else 'test.json'
    data = render_template(template)
    response = make_response(data)
    response.headers['Content-Type'] = match

    return response

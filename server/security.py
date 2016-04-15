

from functools import wraps

from flask.ext.httpauth import HTTPBasicAuth
from flask import Blueprint, current_app, jsonify, request, abort
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired

from server.models import User, get_user


auth = HTTPBasicAuth()
security_bp = Blueprint('auth', __name__)


@security_bp.route('/login')
@auth.login_required
def get_auth_token():
    token = generate_auth_token(current_app.user)
    return jsonify({'token': token.decode('ascii'),
                    'name': current_app.user.name})


@auth.verify_password
def verify_user_password(username, password):
    user = get_user(username)
    if not user or not user.password == password:
        return False
    current_app.user = user
    return True


def auth_token_required(fn):
    @wraps(fn)
    def decorated(*args, **kwargs):
        token = request.headers.get(
            current_app.config['TOKEN_AUTHENTICATION_HEADER'], None)

        if token is None:
            abort(401, 'Unauthorized Access. Token is not specified')

        user = verify_auth_token(token)
        if user:
            current_app.user = user
            return fn(*args, **kwargs)
        abort(401, 'Unauthorized Access. Incorrect token')
    return decorated


def generate_auth_token(user):
    s = Serializer(current_app.config['SECRET_KEY'],
                   expires_in=current_app.config['TOKEN_EXPIRATION_TIME'])
    return s.dumps({'name': user.name})


def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except SignatureExpired:
        return None
    except BadSignature:
        return None
    user = User.query.get(data['id'])
    return user

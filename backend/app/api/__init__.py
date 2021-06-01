from flask import Blueprint

api = Blueprint("api", __name__, url_prefix="/api")

from .users_route import users_bp
api.register_blueprint(users_bp)

from .auth_route import auth_bp
api.register_blueprint(auth_bp)

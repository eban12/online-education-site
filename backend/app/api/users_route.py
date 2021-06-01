from flask import Blueprint, jsonify
from flask_restx import Resource, Api

users_bp = Blueprint('users', __name__, url_prefix='users')
users_api = Api(users_bp)

@users_api.route("/")
class UsersList(Resource):
    def get(self):
        return {"test_key": "test_value"}
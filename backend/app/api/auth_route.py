from flask import Blueprint, request, make_response
from flask_restx import Resource, Api
from werkzeug.security import check_password_hash
from app.models import User
import jwt
import datetime
from app import app

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
auth_api = Api(auth_bp)

@auth_api.route("/")
class Auth(Resource):
    def get(self):
        auth = request.authorization

        if not auth or not auth.username or not auth.password:
            return make_response("Could not verify", 401, {'WWW-Authenticate': 'Basic realm="Login required"'})

        user = User.query.filter_by(email=auth.username).first()

        if not user:
            return make_response("Could not verify", 401, {'WWW-Authenticate': 'Basic realm="Login required"'})
        
        if check_password_hash(user.password, auth.password):
            token = jwt.encode({
                        'public_id': user.public_id,
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=120)     
                    }, app.config['SECRET_KEY'], algorithm="HS256")
            return {
                    "token": token, 
                    "user_id": user.public_id
                }
        
        return make_response("Could not verify", 401, {'WWW-Authenticate': 'Basic realm="Login required"'})


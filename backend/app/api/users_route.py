from flask import Blueprint, request
from flask_restx import Resource, Api
from werkzeug.security import generate_password_hash
from app.api.helpers import *
from app.models import *
from sqlalchemy import exc
from psycopg2.errors import UniqueViolation
import uuid

users_bp = Blueprint('users', __name__, url_prefix='users')
users_api = Api(users_bp)

instructors_bp = Blueprint("instructors", __name__, url_prefix="/instructors")
instructors_api = Api(instructors_bp)

@users_api.route("/")
class UsersList(Resource):
    @token_required
    def get(self, current_user):
        if not current_user.role == 'admin':
            return {"message": "Can not perform function!"}, 401

        users = [build_user_dictionary(user) for user in User.query.all()]
        return {"users": users}
    
    def post(self):
        data = request.get_json()

        required = {"first_name", "last_name", "email", "password"}
        if set(data.keys()).intersection(required) != required:
            return {"message": "Invalid request!"}, 400

        hashed_password = generate_password_hash(data['password'], method='sha256')
        new_user = User(public_id=str(uuid.uuid4()), 
                        first_name=data['first_name'], 
                        last_name=data['last_name'], 
                        email=data['email'], 
                        password=hashed_password, 
                        role='student')
        try:
            db.session.add(new_user)
            db.session.commit()
        except exc.IntegrityError as e:
            if isinstance(e.orig, UniqueViolation):
                return {"message": "Email already exists"}, 400
            return {"message": "Invalid data!"}, 400
        return {"message": "New user created!"}

@users_api.route('/<public_id>')
@instructors_api.route("/<public_id>")
class UserSingle(Resource):
    @token_required
    def get(self, public_id, current_user):
        user = User.query.filter_by(public_id=public_id).first()

        if not user:
            return {"message": "No user found"}, 404

        if current_user.role != 'admin' and  user.public_id != current_user.public_id:
            return {"message": "Can not perform function!"}, 401

        return {"user": build_user_dictionary(user)}

    @token_required
    def put(self, current_user, public_id):
        user = User.query.filter_by(public_id=public_id).first()
        data = request.get_json()

        if not user:
            return {"message": "No user found"}, 404
        
        if current_user.public_id != public_id:
            return {"message": "Can not perform function!"}, 401
        
        if 'password' in data:
            hashed_password = generate_password_hash(data.get('password'), method='sha256')
            user.password = hashed_password
 
        user.first_name = data.get('first_name', user.first_name) 
        user.last_name = data.get('last_name', user.last_name) 
        user.profile_image = data.get('profile_image', user.profile_image)

        db.session.commit()

        return {"message": "User has been updated!"}

    @token_required
    def delete(self, public_id, current_user):
        if current_user.role != 'admin':
            return {"message": "Can not perform function!"}, 401

        user = User.query.filter_by(public_id=public_id).first()

        if not user:
            return {"message": "No user found"}, 404
        
        db.session.delete(user)
        db.session.commit()
        return {"message": "User has been deleted!"}

@instructors_api.route("")
@instructors_api.route("/")
class InstructorsList(Resource):
    @token_required
    def get(self, current_user):
        if current_user.role != 'admin':
            return {"message": "Can not perform function!"}, 401
        
        instructors = db.session.query(User, Instructors).join(User).all()
        return {"instructors": [build_instructors_dictionary(instructor) for instructor in instructors]}


    @token_required
    def post(self, current_user):
        if current_user.role != 'admin':
            return {"message": "Can not perform function!"}, 401
        
        data = request.get_json()

        required = {"first_name", "last_name", "email", "password"}
        if set(data.keys()).intersection(required) != required:
            return {"message": "Invalid request!"}, 400

        hashed_password = generate_password_hash(data['password'], method='sha256')
        new_user = User(public_id=str(uuid.uuid4()), 
                        first_name=data['first_name'], 
                        last_name=data['last_name'], 
                        email=data['email'], 
                        password=hashed_password, 
                        role='instructor')
        try:
            db.session.add(new_user)
            db.session.commit()
        except exc.IntegrityError as e:
            if isinstance(e.orig, UniqueViolation):
                return {"message": "Email already exists"}, 400
            return {"message": "Invalid data!"}, 400
        return {"message": "New user created!"}
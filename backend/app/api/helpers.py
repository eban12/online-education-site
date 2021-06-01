import sys
sys.path.append("..")

from functools import wraps
from flask import request
from app.models import *

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return {"message": "Token is missing!"}, 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return {"message": "Invalid token!"}, 401
        return f(*args, **kwargs, current_user=current_user)

    return decorated

def build_user_dictionary(user):
    return {
            "public_id": user.public_id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "profile_image": user.profile_image,
            "role": user.role,
            "email": user.email,
            "password": user.password 
        }

def build_course_dictionary(course):
    return {
        "id": course.id,
        "name": course.name,
        "description": course.description,
        "created_at": course.created_at.isoformat(' ', 'minutes'),
        "last_updated": course.last_updated.isoformat(' ', 'minutes'),
        "chapters": [
            {"chapter_id": chapter.id, "chapter_title": chapter.title} for chapter in course.chapters
        ]
    }

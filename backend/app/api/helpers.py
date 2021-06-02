from functools import wraps
from flask import request
from app.models import *
from app import app
import jwt

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
        "course_image": course.course_image,
        "created_at": course.created_at.isoformat(' ', 'minutes'),
        "last_updated": course.last_updated.isoformat(' ', 'minutes'),
        "chapters": [build_chapter_dictionary(chapter) for chapter in course.chapters]
    }

def build_instructors_dictionary(instructor):
    user, inst = instructor
    return build_user_dictionary(user)

def build_chapter_dictionary(chapter):
    return {
        "id": chapter.id,
        "title": chapter.title,
        "chapter_number": chapter.chapter_number,
    }
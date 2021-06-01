from flask import Blueprint, request
from flask_restx import Resource, Api
from app.api.helpers import build_course_dictionary, token_required, build_instructors_dictionary
from app.models import *
import datetime

courses_bp = Blueprint("courses", __name__, url_prefix="courses")
courses_api = Api(courses_bp)

@courses_api.route('/')
class CoursesList(Resource):
    def get(self):
        courses = [build_course_dictionary(course) for course in Course.query.all()]
        return {"courses": courses}

    @token_required
    def post(self, current_user):
        if current_user.role != 'admin':
            return {"message": "Can not perform function!"}, 401
        
        data = request.get_json()

        if "name" not in data:
            return {"message": "Course name is missing!"}, 400

        new_course = Course(name=data['name'],
                            description=data.get('description', ''),
                            course_image=data.get('course_image', ''),
                            created_at=datetime.datetime.now(),
                            last_updated=datetime.datetime.now())
        db.session.add(new_course)
        db.session.commit()
        return {"message": "Course has been created!"}

@courses_api.route('/<int:course_id>')
class CourseSingle(Resource):
    def get(self, course_id):
        course = Course.query.filter_by(id=course_id).first()
        if not course:
            return {"message": "Resource not found!"}, 404
        
        return {"course": build_course_dictionary(course)}
    
    @token_required
    def put(self, course_id, current_user):
        if current_user.role != 'admin':
            return {"message": "Can not perform function!"}, 401
        
        course = Course.query.filter_by(id=course_id).first()
        if not course:
            return {"message": "Resource not found!"}, 404
        
        data = request.get_json()

        if "name" in data or "description" in data or "course_image" in data:
            course.name = data["name"] if "name" in data else course.name
            course.description = data["description"] if "description" in data else course.description
            course.course_image = data["course_image"] if "course_image" in data else course.course_image
            course.last_updated = datetime.datetime.now()
            db.session.commit()
            return {"message": "Course has been updated!"}
        
        return {"message": "Invalid request!"}, 400

    @token_required
    def delete(self, course_id, current_user):
        pass

@courses_api.route('/<int:course_id>/instructors')
class CourseInstructors(Resource):
    def get(self, course_id):
        course = Course.query.filter_by(id=course_id).first()

        if not course:
            return {"message": "Resource not found!"}, 404
        
        instructors = db.session.query(User, Instructors).join(User).filter(Instructors.course_id==course_id).all()
        return {"insttructors": [build_instructors_dictionary(instructor) for instructor in instructors]}

@courses_api.route('/<int:course_id>/instructors/<instructor_id>')
class CourseInstructor(Resource):
    @token_required
    def put(self, course_id, instructor_id, current_user):
        if current_user.role != 'admin':
            return {"message": "Can not perform function!"}, 401
        
        course = Course.query.filter_by(id=course_id).first()
        if not course:
            return {"message": "Course not found!"}, 404
        
        instructor = User.query.filter_by(public_id=instructor_id).first()
        if not instructor:
            return {"message": "Instructor not found!"}, 404

        new_instructor = Instructors(course_id=course_id, user_id=instructor.id)
        db.session.add(new_instructor)
        db.session.commit()

        return {"message": "Instructor has been assigned to course!"}

    @token_required
    def delete(self, course_id, instructor_id, current_user):
        if current_user.role != 'admin':
            return {"message": "Can not perform function!"}, 401
        
        user = User.query.filter_by(public_id=instructor_id).first()
        if not user:
            return {"message": "Instructor not found!"}, 404

        instructor = Instructors.query.filter_by(course_id=course_id, user_id=user.id).first()
        if not instructor:
            return {"message": "Instructor was not found!"}, 404

        db.session.delete(instructor)
        db.session.commit()

        return {"message": "Instructor has been unassigned from course!"}

@courses_api.route('/<int:course_id>/chapters')
class ChaptersList(Resource):
    def get(self, course_id):
        pass 

    def post(self, course_id):
        pass
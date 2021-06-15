from flask import Blueprint, request
from flask_restx import Resource, Api
from app.api.helpers import *

progress_bp = Blueprint("progress", __name__, url_prefix="/progress")
progress_api = Api(progress_bp)

@progress_api.route("/")
class ProgressList(Resource):
    @token_required
    def get(self, current_user):
        progresses = Progress.query.filter_by(user_id=current_user.id).all()
        return {"progresses": [build_pregress_dictionary(progress) for progress in progresses]}

@progress_api.route("/course/<int:course_id>")
class ProgressSingle(Resource):
    @token_required
    def get(self, course_id, current_user):
        progress = Progress.query.filter_by(user_id=current_user.id, course_id=course_id).first()

        if not progress:
            return {"message": "User hasn't started this course yet"}, 404
        
        return {"progress": build_pregress_dictionary(progress)}

    @token_required
    def put(self, course_id, current_user):
        data = request.get_json()

        if "current_section" not in data:
            return {"message": "Missing data!"}, 400
        
        section_id = data["current_section"]

        section = Section.query.filter_by(id=section_id).first()
        if not section:
            return {"message": "Section not found!"}, 404

        progress = Progress.query.filter_by(course_id=course_id, user_id=current_user.id).first()

        if progress:
            progress.current_section = section_id
        else:
            new_progress = Progress(user_id=current_user.id, course_id=course_id, current_section=section.id)
            db.session.add(new_progress)
            
        db.session.commit()

        return {"message": "Progress has been saved!"}
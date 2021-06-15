from app import db
from datetime import datetime
from sqlalchemy.orm import backref

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))
    profile_image = db.Column(db.String(100))
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(10), default="student")
    comments = db.relationship('Comment', backref='user', lazy=True)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    course_image = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, nullable=False)
    last_updated = db.Column(db.DateTime)
    chapters = db.relationship('Chapter', backref='course', lazy=True, cascade="all,delete")

class Instructors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chapter_number = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    sections = db.relationship('Section', backref='chapter', lazy=True, cascade="all,delete")

class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)
    section_number = db.Column(db.Integer, nullable=False)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.id'), nullable=False)
    comments = db.relationship('Comment', backref='section', lazy=True, cascade="all,delete")

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'), nullable=False)

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    current_section = db.Column(db.Integer, db.ForeignKey('section.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=backref("progress", cascade="all,delete"))
    course = db.relationship('Course', backref=backref("progress", cascade="all,delete"))
    section = db.relationship('Section', backref=backref("progress", cascade="all,delete"))
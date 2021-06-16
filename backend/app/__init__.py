from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash
import os
import uuid
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config.from_mapping (
    SECRET_KEY = 'secretkey',
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL").replace('postgres://', 'postgresql://'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from .api import api
app.register_blueprint(api)

@app.cli.command("init_admin")
def init_admin():
    from app.models import User
    admin = User(public_id=str(uuid.uuid4()), first_name="John", last_name="Doe", email="admin@admin.com", role='admin', password=generate_password_hash("adminPass"))
    try:
        db.session.add(admin)
        db.session.commit()
    except Exception:
        print("Admin already created")
        return
    print("Succesfully created Admin")
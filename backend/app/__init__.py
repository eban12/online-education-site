from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config.from_mapping (
    SECRET_KEY = 'secretkey',
    # SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL").replace('postgres://', 'postgresql://'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

db = SQLAlchemy(app)

from .api import api
app.register_blueprint(api)

@app.cli.command("init-db")
def init_db_command():
    db.create_all()


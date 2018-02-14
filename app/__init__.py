from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)

UPLOAD_FOLDER = "./app/static/images"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(["jpg", "JPG", "JPEG", "jpeg", "png", "PNG"])

from app import views, models 


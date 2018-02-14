from flask import Flask, render_template, redirect, url_for, request, session
from werkzeug.utils import secure_filename
from app import app, db, ALLOWED_EXTENSIONS, UPLOAD_FOLDER
from app.models import User
import os

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() \
            in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
	users = User.query.all()
	return render_template("index.html", title="Flask - File - Upload", users=users)

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        username = request.form["username"]
        file = request.files["file"]
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            saving = User(username=username, name=filename)
            db.session.add(saving)
            db.session.commit()
            return redirect(url_for('index', filename=filename))
    return render_template("upload.html", title="Upload - New - File")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
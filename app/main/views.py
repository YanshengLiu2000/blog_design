from flask_sqlalchemy import SQLAlchemy

from . import main
from flask import render_template
from app import app, models
@main.route('/',methods=['GET'])
def home():
    diary_dict={}

    db = SQLAlchemy(app)
    for i in db.session.query(models.Diary).all():
        print(i.tags)
    return render_template("home.html")

@main.route('/resume',methods=['GET'])
def resume():
    return render_template("resume.html")

@main.route('/about_me', methods=['GET'])
def about_me():
    return render_template("about_me.html")
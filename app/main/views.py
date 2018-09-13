from flask_sqlalchemy import SQLAlchemy

from . import main
from flask import render_template
from app import app, models

db = SQLAlchemy(app)

@main.route('/',methods=['GET'])
def home():
    diary_dict={}

    # db = SQLAlchemy(app)
    for i in db.session.query(models.Diary).all():
        print(i.name)
    diary_list=db.session.query(models.Diary).all()
    return render_template("home.html",diary_list=diary_list[::-1])

@main.route('/resume',methods=['GET'])
def resume():
    return render_template("resume.html")

@main.route('/about_me', methods=['GET'])
def about_me():
    return render_template("about_me.html")

@main.route('/diary_list', methods=['GET'])
def diary_list():
    return render_template("diary_list.html")

# @main.route('/diary/<id>', methods=['GET'])
# def diary_detail(id):
#     diary=db.session.query(models.Diary).get(id)
#     print("TEST!!!!id == ",id)
#     print("diary ==",diary)
#     return render_template('diary_details.html',diary=diary)
@main.route('/test',methods=['GET'])
def diary_detail():
    return render_template('diary_details.html')
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# from app import app

db = SQLAlchemy(app)


class Diary(db.Model):
    __tablename__ = 'diary'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    # relations=relationship('Relation',back_populates='diary')
    tags = db.relationship('Tag', back_populates='diary')
    date = db.Column(db.String)
    content = db.Column(db.TEXT)
    def __repr__(self):
        return "<Diary ({})>".format(self.name, self.id)


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    diary = db.relationship('Diary', back_populates='tags')
    diary_id = db.Column(db.Integer, db.ForeignKey(Diary.id))

    def __repr__(self):
        return "<Tag ({}) id={}>".format(self.name, self.id)




# diary_folder = os.path.join(os.path.join(basedir, 'static'), 'diary')#C:\Users\ylxh5\Documents\blog_design\app\static\diary
#
# tags = ('title:', 'tags:', 'date:', 'content:')
# diary_collections=[]
# for file in os.listdir(diary_folder):
#     file_dir = os.path.join(diary_folder, file)
#     diary_dict = {}
#     with open(file_dir) as f:
#         lines = f.readlines()
#         flag = 0
#         for line in lines:
#             line = line.strip('\n\r')
#             if not line:
#                 continue
#             if line in tags:
#                 tag=line.strip(':')
#                 diary_dict[tag]=''
#             else:
#                 if tag=='tags':
#                     diary_dict[tag] = line.lstrip().split(';')
#                 else:
#                     diary_dict[tag]=diary_dict[tag]+line.lstrip()+'\n\r'
#         diary_collections.append(diary_dict)
#
#
# db.drop_all()
# db.create_all()
# insert_list=[]
# for diary in diary_collections:
#     temp_diary=Diary(name=diary['title'], date=diary['date'], content=diary['content'])
#     temp_diary.tags=[Tag(name=i) for i in diary['tags']]
#     insert_list.append(temp_diary)
# db.session.add_all(insert_list)
# db.session.commit()
# #
# for i in db.session.query(Diary).all():
#     print(i.tags)

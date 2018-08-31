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


# print("========testing============")
# db.drop_all()
# db.create_all()
# # diarys=[Diary(name='d1'),Diary(name='d2'),Diary(name='d3')]
# # for diary in diarys:
# #     diary.tags=[Tag(name=str(diary)+'1'),Tag(name=str(diary)+'2')]
# # db.session.add_all(diarys)
# # db.session.commit()
# #
# for i in db.session.query(Diary).all():
#     print(i.tags)



print(basedir)

diary_folder = os.path.join(os.path.join(basedir, 'static'), 'diary')
print(diary_folder)

tags = ('title:', 'tags:', 'date:', 'content:')
for file in os.listdir(diary_folder):
    file_dir = os.path.join(diary_folder, file)
    diary_dict = {}
    with open(file_dir) as f:
        lines = f.readlines()
        flag = 0
        for line in lines:
            line = line.strip('\n\r')
            if not line:
                continue
            print(line)
            if line in tags:
                tag=line.strip(':')
                diary_dict[tag]=''
            else:
                if tag=='tags':
                    diary_dict[tag] = line.lstrip().split(';')
                else:
                    diary_dict[tag]=diary_dict[tag]+line.lstrip()+'\n\r'
        for i in diary_dict:
            print(i)
            print(diary_dict[i])
    break

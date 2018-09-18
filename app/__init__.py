import os
from flask import Flask



app= Flask(__name__)

from app.main import main as main_blueprint
app.register_blueprint(main_blueprint)

from app.admin import admin as admin_bluepoint
app.register_blueprint(admin_bluepoint, url_prefix='')

basedir=os.path.abspath(os.path.dirname(__file__))

# app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'test.db')
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True



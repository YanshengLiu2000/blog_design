import os
from flask import Flask



app= Flask(__name__)

from app.main import main as main_blueprint
app.register_blueprint(main_blueprint)

from app.admin import admin as admin_bluepoint
app.register_blueprint(admin_bluepoint, url_prefix='')
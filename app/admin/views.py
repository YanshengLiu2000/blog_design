from . import admin

@admin.route('/login',methods=['GET'])
def login():
    return"<h1>This is login in admin!</h1>"


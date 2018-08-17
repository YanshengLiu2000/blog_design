from . import main

@main.route('/',methods=['GET'])
def home():
    return"<h1>This is home in main!</h1>"
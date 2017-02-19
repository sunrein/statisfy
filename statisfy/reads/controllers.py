from flask import Blueprint

reads_blueprint = Blueprint('reads', __name__)

@reads_blueprint.route('/', methods=['GET'])
def index():
    return "All those things I read"

def create():
    return "I want to catalogue this book I just finished. Woo!"

def update():
    return "I have pertinent new information about this book I read. I thought it was like a 4 star, but now I think it is a 2"

def show():
    return "specific info about my read. Necessary?"

def destroy():
    return "I decided that I did not read this book this year"

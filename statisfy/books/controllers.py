from flask import Blueprint

book_blueprint = Blueprint('book', __name__)

@book_blueprint.route('/', methods=['GET'])
def index():
    return "Main"

def create():
    return "New book :D"

def show():
    return "I wanna know all about this one book"

def update():
    return "Should we have this?"

def destroy():
    return "I don't know if we should have this route."

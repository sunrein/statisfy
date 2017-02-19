from flask import Blueprint

acquisition_blueprint = Blueprint('acquisition', __name__)

@acquisition_blueprint.route('/', methods=['GET'])
#users/user_id/acquisitions

def index():
    return "all those books you bought"

def create():
    return "you just bought a new book. Wow!"

def update():
    return "I forgot this detail about the book I just bought"

def destroy():
    return "I want to erase the shameful evidence of this purchase for some reason :|"

def show():
    return "is this route necessary? Maybe I just want to see details about one acquisition. Maybe I don't."

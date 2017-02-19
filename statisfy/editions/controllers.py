from flask import Blueprint

edition_blueprint = Blueprint('edition', __name__)

@edition_blueprint.route('/', methods=['GET'])
def index():
    return "All the editions for a particular book!"
    #"books/book_id/editions"

def create():
    return "I need to add the edition for this book I have"

def update():
    return "maybe I made a mistake?"

def destroy():
    return "should you be able to do this?"

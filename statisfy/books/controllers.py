from flask import Blueprint

book_blueprint = Blueprint('book', __name__)

@book_blueprint.route('/', methods=['GET'])
def index():
    return "Main"

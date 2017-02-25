from flask import Blueprint, session

from statisfy.acquisitions.models import Acquisition

acquisition_blueprint = Blueprint('acquisition', __name__)

@acquisition_blueprint.route('/', methods=['GET'])
#users/user_id/acquisitions

@acquisition_blueprint.route('/acquisitions', methods=['GET'])
def index():
    acquisitions = Acquisition.model.query(user_id=session.get('user_id'))
    page_view = render_template('statisfy/templates/_show_acquisitions', acquisitions=acquisitions)
    return page_view

def create():
    return "you just bought a new book. Wow!"

def update():
    return "I forgot this detail about the book I just bought"

def destroy():
    return "I want to erase the shameful evidence of this purchase for some reason :|"

def show():
    return "is this route necessary? Maybe I just want to see details about one acquisition. Maybe I don't."

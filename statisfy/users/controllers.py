from flask import Blueprint

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/', methods=['GET'])
def create():
    return "You want to join our site? COOL!"

def update():
    return "I just got a cool new email address that I want to use instead"

def destroy():
    return "I don't want an account on this platform anymore"

def show():
    return "it's my awesome profile (or something), yo!"

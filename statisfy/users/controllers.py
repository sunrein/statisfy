from flask import Blueprint, request, redirect, render_template, url_for
from statisfy.users.models import User
from statisfy.templates import template_env

from app import db

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("register", methods=["GET", "POST"])
def create():
    if request.method =='POST':
        user = User(
                    username=request.form['username'],
                    password=request.form['password'],
                    email=request.form['email']
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user.show',
                        user_id=user.id))
    create_form = template_env.get_template("_create_users.html")
    return render_template(create_form)

@user_blueprint.route("user/<int:user_id>", methods=["GET"])
def show(user_id):
    user = User.query.get(user_id)
    user_template = template_env.get_template('_get_user.html')
    page_view = user_template.render(user=user)
    return page_view

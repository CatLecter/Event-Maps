from dependencies import container
from flask import Blueprint, jsonify, render_template
from forms.auth import LoginForm, RegistrationForm
from services.users import UserService

blueprint = Blueprint('auth', __name__, url_prefix='/')

user_service: UserService = container.resolve(UserService)


@blueprint.route('/signin', methods=['GET'])
def sign_in():
    form = LoginForm()
    return render_template('auth/signin.html', form=form)


@blueprint.route('/signout', methods=['GET'])
def sign_out():
    return jsonify({'result': 'sign out'})


@blueprint.route('/signup', methods=['GET'])
def sign_up():
    form = RegistrationForm()
    return render_template('auth/signup.html', form=form)

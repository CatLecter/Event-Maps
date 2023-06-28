from dependencies import container
from flask import (Blueprint, jsonify, redirect, render_template, request,
                   url_for)
from forms.auth import LoginForm, RegistrationForm
from schemes.users import User
from services.users import UserService

blueprint = Blueprint('user', __name__, url_prefix='/user')

user_service: UserService = container.resolve(UserService)


@blueprint.route('/', methods=['POST'])
def add_user():
    form = RegistrationForm()
    if not form.validate_on_submit():
        return redirect(url_for('auth.sign_up'))
    user_data = User(**form.data)
    user: dict | None = user_service.add_user(user_data)
    if not user:
        return request.routing_exception
    return redirect(url_for('auth.sign_in'))


@blueprint.route('/', methods=['GET'])
def get_user():
    user_uuid: str = request.args.get('user_uuid')
    user: dict | None = user_service.get_user(user_uuid)
    if not user:
        return jsonify({'result': 'failed', 'message': f'User with UUID={user_uuid} not found'})
    return jsonify(user)


@blueprint.route('/profile', methods=['POST'])
def get_profile_by_email():
    form = LoginForm()
    if not form.validate_on_submit():
        return redirect(url_for('auth.sign_in'))
    user: dict | None = user_service.get_user_by_email(form.email.data)
    if not user:
        return jsonify({'result': 'failed', 'message': f'User with email={email} not found'})
    return render_template('users/profile.html', current_user=user)


@blueprint.route('/', methods=['PUT'])
def update_user():
    user_uuid: str = request.args.get('user_uuid')
    user_data = User(**request.json)
    user: dict | None = user_service.update_user(user_uuid, user_data)
    if not user:
        return jsonify({'result': 'failed', 'message': f'User with UUID={user_uuid} not found'})
    return jsonify(user)


@blueprint.route('/', methods=['DELETE'])
def delete_user():
    user_uuid: str = request.args.get('user_uuid')
    result: bool = user_service.delete_user(user_uuid)
    if not result:
        return jsonify({'result': 'failed', 'message': f'User with UUID={user_uuid} not found'})
    return jsonify({'result': 'success'})

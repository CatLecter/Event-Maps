from dependencies import container
from flask import Blueprint, render_template
from services.users import UserService

blueprint = Blueprint('home', __name__, url_prefix='/')

user_service: UserService = container.resolve(UserService)


@blueprint.route('/', methods=['GET'])
def home():
    return render_template('home/home.html')

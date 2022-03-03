"""
    user route
"""
from flask import Blueprint
from src.exception.user_already_exists import UserAlreadyExists


user_blueprint = Blueprint("user_blueprint", __name__)


@user_blueprint.app_errorhandler(UserAlreadyExists)
def handle_user_already_exists_exception(exception: UserAlreadyExists):
    """ handle user already exists exception """
    return exception.get_reponse()

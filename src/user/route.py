"""
    user route
"""
from flask import Blueprint
from src.exception import UserAlreadyExistsException



user_blueprint = Blueprint("user_blueprint", __name__)


@user_blueprint.app_errorhandler(UserAlreadyExistsException)
def handle_user_already_exists_exception(exception: UserAlreadyExistsException):
    """ handle user already exists exception """
    return exception.get_reponse()

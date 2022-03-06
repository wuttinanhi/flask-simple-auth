"""
    user route
"""
from flask import Blueprint
from src.decorator.use_template_decorator import use_template
from src.exception import UserAlreadyExistsException
from src.decorator.decorator_logged_in import logged_in
from src.security.service import SecurityService
from src.exception.user_not_found import UserNotFoundException

user_blueprint = Blueprint("user", __name__, url_prefix="/user")



@user_blueprint.route("/", methods=["GET"])
@logged_in()
@use_template("user.html")
def get_user():
    """ user route """
    user = SecurityService.get_user()
    return {
        "id": user.id,
        "username": user.username
    }


@user_blueprint.app_errorhandler(UserAlreadyExistsException)
def handle_user_already_exists_exception(exception: UserAlreadyExistsException):
    """ handle user already exists exception """
    return exception.get_reponse()


@user_blueprint.app_errorhandler(UserNotFoundException)
def handle_user_not_found_exception(exception: UserNotFoundException):
    """ handle user not found exception """
    return exception.get_reponse()

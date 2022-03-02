"""
    auth module
"""
from http.client import CREATED, OK
from flask import Blueprint, make_response, request
from src.user.user import UserService, User
from src.exception.auth_fail import AuthFail


auth_blueprint = Blueprint("auth_blueprint", __name__, url_prefix="/auth")


class AuthService():
    """
    class AuthService
    """

    @staticmethod
    def login(username, password):
        """ login user """
        try:
            user = User.get_query().filter(
                User.username == username
            ).filter(
                User.password == password
            ).one()
            return user
        except:
            raise AuthFail()

    @staticmethod
    def register(username, password):
        """ register user"""
        user = UserService.create_user(username, password)
        return user


@auth_blueprint.route("/login", methods=["POST"])
def login():
    """ login route """
    data = request.get_json(force=True)
    username = data["username"]
    password = data["password"]
    user = AuthService.login(username, password)
    response = make_response({
        "id": user.id,
        "username": user.username
    })
    response.status = OK
    return response


@auth_blueprint.route("/register", methods=["POST"])
def register():
    """ register route """
    data = request.get_json(force=True)
    username = data["username"]
    password = data["password"]
    user = AuthService.register(username, password)
    response = make_response({"id": user.id})
    response.status = CREATED
    return response


@auth_blueprint.app_errorhandler(AuthFail)
def handle_auth_fail(exception: AuthFail):
    """ auth fail exception handler """
    return exception.get_reponse()

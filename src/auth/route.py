"""
    auth route
"""
from http.client import CREATED, OK
from flask import Blueprint, make_response, request, session
from src.auth.dto import AuthLoginDto, AuthRegisterDto
from src.exception import AuthFailExcepion
from src.decorator.view_redirect_decorator import view_redirect
from src.auth.service import AuthService


auth_blueprint = Blueprint("auth_blueprint", __name__, url_prefix="/auth")


def parse_request():
    """ parse request wrapper """
    if request.is_json is True:
        return request.get_json()
    return request.form


@auth_blueprint.route("/login", methods=["POST"])
@view_redirect("user.get_user")
def login():
    """ login route """
    # parse data
    schema = AuthLoginDto()
    data = schema.load(parse_request())
    username = data.username
    password = data.password

    # perform login
    user = AuthService.login(username, password)

    # set session to user id
    session["user_id"] = user.id

    # create response
    response = make_response({
        "id": user.id,
        "username": user.username
    })
    response.status = OK
    return response


@auth_blueprint.route("/register", methods=["POST"])
def register():
    """ register route """

    # parse data
    schema = AuthRegisterDto()
    data = schema.load(request.get_json(force=True))
    username = data.username
    password = data.password

    # register user
    user = AuthService.register(username, password)

    # create response
    response = make_response({"id": user.id})
    response.status = CREATED
    return response


@auth_blueprint.route("/logout", methods=["GET"])
def logout():
    """ logout route """
    # remove user id from session
    session.pop("user_id", None)

    # create response
    response = make_response({"status": OK})
    response.status = OK
    return response


@auth_blueprint.app_errorhandler(AuthFailExcepion)
def handle_auth_fail(exception: AuthFailExcepion):
    """ auth fail exception handler """
    return exception.get_reponse()

"""
    auth route
"""
from http.client import CREATED, OK
from flask import Blueprint, make_response, request
from src.auth.dto import AuthLoginDto, AuthRegisterDto
from src.exception.auth_fail import AuthFail
from . import AuthService

auth_blueprint = Blueprint("auth_blueprint", __name__, url_prefix="/auth")


@auth_blueprint.route("/login", methods=["POST"])
def login():
    """ login route """
    schema = AuthLoginDto()
    data = schema.load(request.get_json(force=True))
    username = data.username
    password = data.password

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
    schema = AuthRegisterDto()
    data = schema.load(request.get_json(force=True))
    username = data.username
    password = data.password

    user = AuthService.register(username, password)

    response = make_response({"id": user.id})
    response.status = CREATED

    return response


@auth_blueprint.app_errorhandler(AuthFail)
def handle_auth_fail(exception: AuthFail):
    """ auth fail exception handler """
    return exception.get_reponse()

"""
    auth module
"""
from http.client import INTERNAL_SERVER_ERROR
from typing import Any
from flask import Blueprint, make_response, request

auth_blueprint = Blueprint("auth_blueprint", __name__, url_prefix="/auth")

MOCKED_DATABASE = {
    "admin": "adminpwd",
    "user": "userpwd"
}


class AuthService:
    """
    class AuthService
    """

    @staticmethod
    def login(username, password):
        """ login user """
        if MOCKED_DATABASE.get(username):
            if MOCKED_DATABASE.get(username) == password:
                return True
            return False
        raise RuntimeError("User not found!")

    @staticmethod
    def register(username, password):
        """ register user"""
        MOCKED_DATABASE[username] = password
        return 1


@auth_blueprint.route("/login", methods=["POST"])
def login():
    """ login route """
    data = request.get_json(force=True)
    username = data["username"]
    password = data["password"]
    return {"status": 200, "auth_status": AuthService.login(username, password)}


@auth_blueprint.route("/register", methods=["POST"])
def register():
    """ register route """
    data = request.get_json(force=True)
    username = data["username"]
    password = data["password"]
    return {"status": 201, "id": AuthService.register(username, password)}


@auth_blueprint.errorhandler(RuntimeError)
def handle_runtime_error(error: Any):
    """ runtime exception handler """
    response = make_response({"status": 500, "error": type(error).__name__})
    response.status = INTERNAL_SERVER_ERROR
    return response

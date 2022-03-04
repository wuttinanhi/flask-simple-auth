"""
    auth route
"""
from http.client import OK
from flask import Blueprint, make_response
from . import SecurityService
from . import logged_in


security_blueprint = Blueprint(
    "security_blueprint",
    __name__,
)


@security_blueprint.route("/user", methods=["GET"])
@logged_in()
def get_user():
    """ user route """
    user = SecurityService.get_user()
    response = make_response({
        "id": user.id,
        "username": user.username
    })
    response.status = OK
    return response

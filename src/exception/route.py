"""
    exception route
"""
# pylint: disable=unused-argument
from http.client import BAD_REQUEST, INTERNAL_SERVER_ERROR, UNAUTHORIZED
from flask import Blueprint,  make_response
from marshmallow.exceptions import ValidationError
from . import ValidationException


exception_handler_blueprint = Blueprint(
    "exception_handler_blueprint",
    __name__
)


@exception_handler_blueprint.app_errorhandler(BAD_REQUEST)
def handle_bad_request_exception(exception):
    """ handle bad request exception (status 400) """
    response = make_response({
        "status": BAD_REQUEST,
        "error": "Bad request."
    })
    response.status = BAD_REQUEST
    return response


@exception_handler_blueprint.app_errorhandler(UNAUTHORIZED)
def handle_unauthorized_exception(exception):
    """ handle unauthorized exception (status 401) """
    response = make_response({
        "status": UNAUTHORIZED,
        "error": "Unauthorized."
    })
    response.status = UNAUTHORIZED
    return response


@exception_handler_blueprint.app_errorhandler(ValidationError)
def handle_validation_error_fail(exception: ValidationError):
    """ validation exception handler """
    ex = ValidationException(exception)
    return ex.get_reponse()


@exception_handler_blueprint.app_errorhandler(INTERNAL_SERVER_ERROR)
@exception_handler_blueprint.app_errorhandler(Exception)
def handle_internal_server_exception(exception: Exception):
    """ handle internal server exception (status 500) """
    response = make_response({
        "status": INTERNAL_SERVER_ERROR,
        "error": "Internal server exception."
    })
    response.status = INTERNAL_SERVER_ERROR
    return response

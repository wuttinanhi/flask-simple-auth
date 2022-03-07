"""
    auth route
"""
from http.client import CREATED, OK
from flask import Blueprint, flash, make_response, redirect, render_template, request, session, url_for
from marshmallow import ValidationError
from src.auth.dto import AuthLoginDto, AuthRegisterDto
from src.exception import AuthFailExcepion
from src.decorator.view_redirect_decorator import view_redirect
from src.auth.service import AuthService
from src.exception.app_exception import AppException
from src.exception.validation_exception import ValidationException
from src.util.parse_request_wrapper import parse_request


auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    """ login route """
    try:
        # if request is GET method return login page
        if request.method == "GET":
            return render_template("login.html")

        # parse data
        schema = AuthLoginDto()
        data = schema.load(parse_request())
        username = data.username
        password = data.password

        # perform login
        user = AuthService.login(username, password)

        # set session to user id
        session["user_id"] = user.id

        # redirect to user page
        return redirect(url_for("user.user"))
    except AppException as exception:
        # flash error and return template
        flash(str(exception.message), "error")
        return render_template("login.html")


@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    """ register route """
    try:
        # if request is GET method return register page
        if request.method == "GET":
            return render_template("register.html")

        # parse data
        schema = AuthRegisterDto()
        data = schema.load(parse_request())
        username = data.username
        password = data.password

        # register user
        user = AuthService.register(username, password)

        # set session to user id
        session["user_id"] = user.id

        # redirect to user page
        return redirect(url_for("user.user"))
    except AppException as exception:
        # flash error and return template
        flash(str(exception.message), "error")
        return render_template("register.html")
    except ValidationError as exception:
        # convert to validate error exception
        validation_exception = ValidationException(exception)

        # flash error and return template
        for field, reasons in validation_exception.errors.items():
            for reason in reasons:
                flash(f'{field} {reason}', "error")
        return render_template("register.html")


@auth_blueprint.route("/logout", methods=["GET"])
def logout():
    """ logout route """
    # remove user id from session
    session.pop("user_id", None)

    # redirect to index page
    return redirect(url_for("root"))


@auth_blueprint.app_errorhandler(AuthFailExcepion)
def handle_auth_fail(exception: AuthFailExcepion):
    """ auth fail exception handler """
    return exception.get_reponse()

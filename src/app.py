
"""
    main app
"""
# pylint: disable=unused-argument
from http.client import BAD_REQUEST, INTERNAL_SERVER_ERROR
from flask import Flask, make_response
from marshmallow.exceptions import ValidationError
from src.database import db
from src.auth import auth_blueprint
from src.exception.validation_exception import ValidationException
from src.user import user_blueprint


def create_app():
    """
        create app wrapper
    """
    # create app
    __app = Flask(__name__)

    # register things
    with __app.app_context():
        # register database
        __app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'
        __app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        db.init_app(__app)

        # create table
        db.create_all()

        # register blueprint
        __app.register_blueprint(auth_blueprint)
        __app.register_blueprint(user_blueprint)

    # return configured app
    return __app


app = create_app()


@app.route("/")
def hello_world():
    """
    root route
    """
    return "<p>Hello, World!</p>"


@app.errorhandler(400)
def handle_bad_request_exception(exception):
    """ handle bad request exception (status 400) """
    response = make_response({
        "status": 400,
        "error": "Bad request."
    })
    response.status = BAD_REQUEST
    return response


@app.errorhandler(500)
def handle_internal_server_exception(exception):
    """ handle internal server exception (status 500) """
    response = make_response({
        "status": 500,
        "error": "Internal server exception."
    })
    response.status = INTERNAL_SERVER_ERROR
    return response


@app.errorhandler(ValidationError)
def handle_validation_error_fail(exception: ValidationError):
    """ validation exception handler """
    ex = ValidationException(exception)
    return ex.get_reponse()

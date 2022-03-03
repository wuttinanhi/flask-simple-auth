"""
    main app
"""
from http.client import BAD_REQUEST, INTERNAL_SERVER_ERROR
from flask import Flask, make_response
from src.database import db
from src.auth import auth_blueprint
from src.user import user_blueprint


def create_app():
    # create app
    app = Flask(__name__)

    # register things
    with app.app_context():
        # register database
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        db.init_app(app)

        # create table
        db.create_all()

        # register blueprint
        app.register_blueprint(auth_blueprint)
        app.register_blueprint(user_blueprint)

    # return configured app
    return app


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

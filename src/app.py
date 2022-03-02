"""
    main app
"""
from http.client import INTERNAL_SERVER_ERROR
from flask import Flask, make_response
from src.database import db
from src.auth.auth import auth_blueprint
from src.user.user import user_blueprint


def create_app():
    # create app
    app = Flask(__name__)

    # register database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)

    # register things
    with app.app_context():
        # create table
        db.create_all()

        # register blueprint
        app.register_blueprint(auth_blueprint)
        app.register_blueprint(user_blueprint)

    return app


app = create_app()


@app.route("/")
def hello_world():
    """
    root route
    """
    return "<p>Hello, World!</p>"


@app.errorhandler(500)
def handle_internal_server_exception(exception):
    """ handle internal server exception (status 500) """
    response = make_response({
        "status": 500,
        "error": type(exception).__name__
    })
    response.status = INTERNAL_SERVER_ERROR
    return response

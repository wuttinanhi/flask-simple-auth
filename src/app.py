
"""
    main app
"""
# pylint: disable=unused-argument
import random
import string
from flask import Flask
from src.auth import auth_blueprint
from src.database import db
from src.exception import exception_handler_blueprint
from src.security import security_blueprint
from src.user import user_blueprint


def create_app():
    """
        create app wrapper
    """
    # create app
    __app = Flask(__name__)

    # register things
    with __app.app_context():
        # assign session secret
        session_secret = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=5)
        )
        __app.secret_key = session_secret

        # register database
        __app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'
        __app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        db.init_app(__app)

        # create table
        db.create_all()

        # register blueprint
        __app.register_blueprint(auth_blueprint)
        __app.register_blueprint(user_blueprint)
        __app.register_blueprint(exception_handler_blueprint)
        __app.register_blueprint(security_blueprint)

    # return configured app
    return __app


app = create_app()


@app.route("/")
def hello_world():
    """ root route """
    return "<p>Hello, World!</p>"

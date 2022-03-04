"""
    decorator logged in
"""
from functools import wraps
from flask import session
from werkzeug.exceptions import Unauthorized


def logged_in():
    """ decorator logged in """

    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            user = session.get("user_id")

            if user is None:
                raise Unauthorized()

            return func(*args, **kwargs)
        return decorated_function

    return decorator

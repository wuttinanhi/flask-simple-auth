"""
    view redirect decorator
"""
from functools import wraps
from flask import redirect, request, url_for


def view_redirect(to_url: str):
    """ view redirect decorator """

    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            # if request content type is json then return json
            if request.is_json is True:
                return func(*args, **kwargs)

            # process request
            func(*args, **kwargs)

            # redirect to target url
            return redirect(url_for(to_url))

        return decorated_function
    return decorator

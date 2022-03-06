"""
    use template decorator
"""
from functools import wraps
from flask import Response, make_response, render_template, request


def use_template(template: str):
    """ use template decorator """

    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            # get return value from route
            return_value = func(*args, **kwargs)

            # return json of request content type is json
            if isinstance(return_value, dict) is True and (request.is_json is True):
                return make_response(return_value)

            # data dict variable for render template
            data = {}

            # if type is dict use it directly
            # if not convert json to dict
            if isinstance(return_value, dict) is True:
                data = return_value
            else:
                return_value: Response
                data = return_value.get_json()

            # make template reponse
            resp = make_response(render_template(template, **data))
            return resp

        return decorated_function
    return decorator

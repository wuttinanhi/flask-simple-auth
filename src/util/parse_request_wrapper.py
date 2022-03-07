"""
    parse request wrapper function
"""
from flask import request


def parse_request():
    """ parse request wrapper """
    if request.is_json is True:
        return request.get_json()
    return request.form

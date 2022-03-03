"""
    validation exception class
"""
from http.client import BAD_REQUEST
from flask import make_response
from marshmallow.exceptions import ValidationError
from src.exception.app_exception import AppException


class ValidationException(AppException):
    """
        validation exception class
    """

    def __init__(self, exception: ValidationError, *args: object) -> None:
        super().__init__(*args)
        self.set_status(BAD_REQUEST)
        self.set_message("Bad request.")
        self.errors = exception.messages

    def get_reponse(self):
        response = make_response({
            "status": self.status,
            "message": self.message,
            "errors": self.errors
        })
        response.status_code = self.status
        return response

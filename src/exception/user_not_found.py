"""
    user not found exception class
"""
from http.client import NOT_FOUND
from src.exception.app_exception import AppException


class UserNotFoundException(AppException):
    """
        user not found exception class
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.set_status(NOT_FOUND)
        self.set_message("username not found.")

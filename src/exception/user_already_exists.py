from http.client import CONFLICT
from src.exception.app_exception import AppException


class UserAlreadyExists(AppException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.set_status(CONFLICT)
        self.set_message("username already exists.")

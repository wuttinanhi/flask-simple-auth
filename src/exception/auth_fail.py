from http.client import UNAUTHORIZED
from src.exception.app_exception import AppException


class AuthFail(AppException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.set_status(UNAUTHORIZED)
        self.set_message("Invalid authentication.")

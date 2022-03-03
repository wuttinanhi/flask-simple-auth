"""
    default exception class
"""
from flask import make_response


class AppException(Exception):
    """
        default exception class
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.status: int = None
        self.message: str = None

    def set_status(self, status: int):
        """ set status code for exception"""
        self.status = status

    def set_message(self, message: str):
        """ set message for exception"""
        self.message = message

    def get_reponse(self):
        """ get response return to user """
        response = make_response({
            "status": self.status,
            "message": self.message
        })
        response.status_code = self.status
        return response

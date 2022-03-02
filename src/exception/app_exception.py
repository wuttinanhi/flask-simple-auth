from flask import make_response


class AppException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.status: int = None
        self.message: str = None

    def set_status(self, status: int):
        self.status = status

    def set_message(self, message: str):
        self.message = message

    def get_reponse(self):
        response = make_response({
            "status": self.status,
            "message": self.message
        })
        response.status_code = self.status
        return response

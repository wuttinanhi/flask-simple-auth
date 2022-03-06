"""
    auth service class
"""
import bcrypt
from src.exception import AuthFailExcepion
from src.user.model import User
from src.user.service import UserService


class AuthService():
    """
    class AuthService
    """

    @staticmethod
    def login(username: str, password: str):
        """ login user """
        try:
            user = User.query.filter(User.username == username).one()
            if bcrypt.checkpw(password.encode("utf-8"), user.password) is False:
                raise AuthFailExcepion()
            return user
        except Exception as exception:
            raise AuthFailExcepion() from exception

    @staticmethod
    def register(username: str, password: str):
        """ register user"""
        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )
        user = UserService.create_user(username, hashed_password)
        return user

"""
    auth service class
"""
from src.exception.auth_fail import AuthFailExcepion
from src.user.service import UserService


class AuthService():
    """
    class AuthService
    """

    @staticmethod
    def login(username: str, password: str):
        """ login user """
        user = UserService.get_user_from_username(username)
        if UserService.compare_password(user, password) is False:
            raise AuthFailExcepion()
        return user

    @staticmethod
    def register(username: str, password: str):
        """ register user"""
        user = UserService.create_user(username, password)
        return user

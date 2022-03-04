"""
    class SecurityService
"""
from flask import session
from src.user import User, UserService


class SecurityService:
    """ class SecurityService """

    @staticmethod
    def get_user() -> User:
        """ get current user in request """
        user_id = session["user_id"]
        user = UserService.get_user_from_id(user_id)
        return user

    @staticmethod
    def is_user_admin(user: User):
        """ check weather given user is admin """
        user = UserService.get_user_from_id(user.id)
        return user.is_admin is True

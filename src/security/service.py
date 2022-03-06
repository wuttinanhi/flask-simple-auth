"""
    class SecurityService
"""
from flask import session
from src.user.model import User
from src.user.service import UserService


class SecurityService:
    """ class SecurityService """

    @staticmethod
    def get_user() -> User:
        """ get current user in request """
        user_id = session.get("user_id")
        user = UserService.get_user_from_id(user_id)
        return user

    @staticmethod
    def is_user_admin(user: User):
        """ check weather given user is admin """
        user = UserService.get_user_from_id(user.id)
        return False

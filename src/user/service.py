"""
    user service class
"""
# pylint: disable=no-member
from __future__ import annotations
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session
from src.database import db
from src.exception import UserAlreadyExistsException
from src.exception.user_not_found import UserNotFoundException
from .model import User


class UserService:
    """
        class UserService
    """

    @staticmethod
    def create_user(username: str, password: str):
        """  create user """
        try:
            session: Session = db.session
            user = User(username, password)
            session.add(user)
            session.commit()
            return user
        except IntegrityError as exception:
            raise UserAlreadyExistsException() from exception

    @staticmethod
    def get_user_from_id(id):
        """ get user from given id """
        try:
            user = User.get_query().filter(User.id == id).one()
            return user
        except Exception as exception:
            raise UserNotFoundException() from exception

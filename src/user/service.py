"""
    user service class
"""
# pylint: disable=no-member
from __future__ import annotations
import bcrypt
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session
from src.database import db
from src.exception import UserAlreadyExistsException
from src.exception.user_not_found import UserNotFoundException
from src.user.model import User


class UserService:
    """
        class UserService
    """

    @staticmethod
    def create_user(username: str, password: str):
        """  create user """
        try:
            hashed_password = bcrypt.hashpw(
                password.encode("utf-8"),
                bcrypt.gensalt()
            )
            session: Session = db.session
            user = User(username, hashed_password)
            session.add(user)
            session.commit()
            return user
        except IntegrityError as exception:
            raise UserAlreadyExistsException() from exception

    @staticmethod
    def get_user_from_id(user_id):
        """ get user from given id """
        try:
            user = User.query.filter(User.id == user_id).one()
            return user
        except Exception as exception:
            raise UserNotFoundException() from exception

    @staticmethod
    def compare_password(user: User, compare_password: str):
        """ compare user and given password """
        return bcrypt.checkpw(compare_password.encode("utf-8"), user.password)

    @staticmethod
    def change_password(user: User, new_password: str):
        """ change user password """
        session: Session = db.session
        user = UserService.get_user_from_id(user.id)
        new_hashed_password = bcrypt.hashpw(
            new_password.encode("utf-8"),
            bcrypt.gensalt()
        )
        user.password = new_hashed_password
        session.commit()
        return user

    @staticmethod
    def get_user_from_username(username: str):
        """ get user by given username """
        try:
            user = User.query.filter(User.username == username).one()
            return user
        except Exception as exception:
            raise UserNotFoundException() from exception

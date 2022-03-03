from __future__ import annotations
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError
from src.database import db
from src.exception.user_already_exists import UserAlreadyExists
from sqlalchemy.orm.session import Session
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
        except IntegrityError:
            raise UserAlreadyExists()

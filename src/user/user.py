"""
    user module
"""
from flask import Blueprint
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError
from src.app import db
from src.exception.user_already_exists import UserAlreadyExists
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.query import Query
from typing import Generic, TypeVar

user_blueprint = Blueprint("user_blueprint", __name__, url_prefix="/user")

#User = TypeVar('User')


class User(db.Model):
    """
        user model
    """
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def get_query():
        session: Session = db.session
        return session.query(User)

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User(id={self.id},name="{self.username}")>'

    def serialize(self):
        return "SERIALIZE"


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


@user_blueprint.app_errorhandler(UserAlreadyExists)
def handle_user_already_exists_exception(exception: UserAlreadyExists):
    return exception.get_reponse()

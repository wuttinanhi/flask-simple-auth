"""
    user model
"""
from __future__ import annotations

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm.query import Query
from src.database import db


class User(db.Model):
    """
        user model
    """
    query: Query[User]

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User(id={self.id},name="{self.username}")>'

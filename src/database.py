"""
    Database Module
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.session import Session


class TypedSQLAlchemy(SQLAlchemy):
    """
        class TypedSQLAlchemy
        for make type hint working
    """
    session: Session


db: TypedSQLAlchemy = SQLAlchemy()

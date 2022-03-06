"""
    auth dto
"""
from marshmallow import Schema, fields, post_load, validate
from src.user.model import User


class AuthLoginDto(Schema):
    """
        auth register dto for user register request
    """
    username = fields.String(
        required=True,
        validate=validate.Length(min=3, max=30),
    )
    password = fields.String(
        required=True,
        validate=validate.Length(min=3, max=100),
    )

    def load(self, data, **kwargs) -> User:
        """ load method """
        return super().load(data, **kwargs)

    @post_load
    def to_object(self, data, **kwargs):  # pylint: disable=unused-argument
        """ turn data into class object """
        return User(**data)


class AuthRegisterDto(AuthLoginDto):
    """
        auth login dto for user login request
    """

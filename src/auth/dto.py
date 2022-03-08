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


class PrivateAuthChangePasswordDto:
    """ private dto for AuthChangePasswordDto """
    current_password: str
    new_password: str


class AuthChangePasswordDto(Schema):
    """
        auth change password dto
    """

    current_password = fields.String(
        required=True,
        validate=validate.Length(min=3, max=100),
    )

    new_password = fields.String(
        required=True,
        validate=validate.Length(min=3, max=100),
    )

    def load(self, data, **kwargs) -> PrivateAuthChangePasswordDto:
        """ load method """
        return super().load(data, **kwargs)

    @post_load
    def to_object(self, data, **kwargs):  # pylint: disable=unused-argument
        """ turn data into class object """
        dto = PrivateAuthChangePasswordDto()
        dto.current_password = data["current_password"]
        dto.new_password = data["new_password"]
        return dto

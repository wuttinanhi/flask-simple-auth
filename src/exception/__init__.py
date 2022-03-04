"""
    exception module
"""
from .app_exception import AppException
from .auth_fail import AuthFailExcepion
from .user_already_exists import UserAlreadyExistsException
from .validation_exception import ValidationException
from .route import exception_handler_blueprint
from .user_not_found import UserNotFoundException

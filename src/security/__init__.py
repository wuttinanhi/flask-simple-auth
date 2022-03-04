"""
    security module
"""
from .service import SecurityService
from .decorator_logged_in import logged_in
from .route import security_blueprint

from src.user.user import UserService, User
from src.exception.auth_fail import AuthFail
import bcrypt


class AuthService():
    """
    class AuthService
    """

    @staticmethod
    def login(username: str, password: str):
        """ login user """
        try:
            user = User.get_query().filter(User.username == username).one()
            if bcrypt.checkpw(password.encode("utf-8"), user.password) == False:
                raise AuthFail()
            return user
        except:
            raise AuthFail()

    @staticmethod
    def register(username: str, password: str):
        """ register user"""
        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )
        user = UserService.create_user(username, hashed_password)
        return user

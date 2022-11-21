import re
from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def check_name_too_short(self, username):
        return len(username) < 3

    def check_name_only_characters(self, username):
        if re.match("^[a-z]+$", username):
            return False
        return True

    def check_password_too_short(self, password):
        return len(password) < 8

    def check_password(self, password):
        if re.match("[a-z]*[0-9][a-z0-9]*", password):
            return False
        return True

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if self.check_name_too_short(username):
            raise UserInputError("Username needs to be at least 3 characters long")

        if self.check_name_only_characters(username):
            raise UserInputError("Name must consist of only a-z")

        if self.check_password_too_short(password):
            raise UserInputError("Password needs to be at least 8 characters long")

        if self.check_password(password):
            raise UserInputError("Password needs at least 1 number and character")
        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa

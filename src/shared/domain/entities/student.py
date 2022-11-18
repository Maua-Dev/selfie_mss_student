import abc
import re
from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterTypeError


class Student(abc.ABC):
    ra: str
    name: str
    email: str
    MIN_NAME_LENGTH: int = 2

    def __init__(self, ra: str, name: str, email: str):

        if not Student.validate_ra(ra):
            raise EntityError('ra')
        self.ra = ra

        if not Student.validate_name(name):
            raise EntityError('name')
        self.name = name

        if not Student.validate_email(email):
            raise EntityError('email')
        self.email = email

    @staticmethod
    def validate_ra(ra: str) -> bool:

        if ra == None:
            return False

        if type(ra) != str:
            raise EntityParameterTypeError('ra must be a string')

        return ra.isdecimal() and len(ra) == 8

    @staticmethod
    def validate_email(email) -> bool:

        if email == None:
            return False

        regex = re.compile(
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        return bool(re.fullmatch(regex, email))

    @staticmethod
    def validate_name(name) -> bool:

        if name == None:
            return False
        
        if len(name) < Student.MIN_NAME_LENGTH:
            return False

        return True

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
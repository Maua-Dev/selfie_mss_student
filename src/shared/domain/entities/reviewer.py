import abc
import re
from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterTypeError

class Reviewer(abc.ABC):
    ra: str
    name: str
    email: str
    active: bool
    MIN_NAME_LENGTH: int = 2

    def __init__(self, ra: str, name: str, email: str, active: bool):
        if not Reviewer.validate_ra(ra):
            raise EntityError('ra')
        self.ra = ra

        if not Reviewer.validate_name(name):
            raise EntityError('name')
        self.name = name

        if not Reviewer.validate_email(email):
            raise EntityError('email')
        self.email = email

        if type(active) != bool:
            raise EntityError('active')
        self.active = active


    @staticmethod
    def validate_ra(ra: str) -> bool:

        if ra == None:
            return False

        if type(ra) != str:
            raise EntityParameterTypeError('ra must be a string')

        return ra.isdecimal() and (len(ra) == 8 or len(ra) == 5)

    @staticmethod
    def validate_email(email) -> bool:

        if email == None:
            return False

        regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

        return bool(re.fullmatch(regex, email))

    @staticmethod
    def validate_name(name) -> bool:

        if name == None:
            return False
        
        if len(name) < Reviewer.MIN_NAME_LENGTH:
            return False

        return True
        
    def __repr__(self):
        return f"Reviewer(ra={self.ra}, name={self.name}, email={self.email}, active={self.active})"

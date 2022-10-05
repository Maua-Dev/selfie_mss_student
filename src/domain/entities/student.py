import abc
from src.helpers.errors.domain_errors import EntityError

class Student(abc.ABC):
    ra: str
    name: str
    email: str
    
    def __init__(self, ra:str, name:str, email:str):
        if (ra == None or len(ra) != 8):
            raise EntityError('ra')
        self.ra = ra
        
        if (len(name) == 0):
            raise EntityError('name')
        self.name = name

        if('@' not in email or '.' not in email):
            raise EntityError('email')
        self.email = email
        
    
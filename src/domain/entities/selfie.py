import abc
import datetime
from src.domain.entities.student import Student
from src.domain.enums.state_enum import STATE
from src.helpers.errors.domain_errors import EntityError


class Selfie(abc.ABC):
    idSelfie: int
    student: Student
    dateUpload: datetime.datetime
    url: str
    state: STATE

    def __init__(self, student: Student, dateUpload: datetime.datetime, url: str, state: STATE, idSelfie: int):
        self.student = student

        if (dateUpload == None and type(dateUpload) != datetime.datetime):
            raise EntityError('dateUpload')
        self.dateUpload = dateUpload

        if (url == None):
            raise EntityError('url')
        self.url = url

        if (state == None or type(state) != STATE):
            raise EntityError('state')
        self.state = state

        if idSelfie == None or type(idSelfie) != int:
            raise EntityError('id')
        self.idSelfie = idSelfie

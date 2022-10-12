import abc
import datetime
from src.domain.entities.student import Student
from src.domain.enums.state_enum import STATE
from src.helpers.errors.domain_errors import EntityError


class Selfie(abc.ABC):
    selfieId: int
    student: Student
    dateUpload: datetime.datetime
    url: str
    state: STATE

    def __init__(self, student: Student, dateUpload: datetime.datetime, url: str, state: STATE, selfieId: int):
        self.student = student

        if (dateUpload == None and type(dateUpload) != datetime.datetime):
            raise EntityError('dateUpload')
        self.dateUpload = dateUpload.isoformat()

        if (url == None):
            raise EntityError('url')
        self.url = url

        if (state == None or type(state) != STATE):
            raise EntityError('state')
        self.state = state

        if selfieId == None or type(selfieId) != int:
            raise EntityError('id')
        self.selfieId = selfieId

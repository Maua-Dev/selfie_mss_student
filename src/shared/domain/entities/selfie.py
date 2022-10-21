import abc
import datetime
from src.shared.domain.entities.student import Student
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.domain_errors import EntityError

class Selfie(abc.ABC):
    idSelfie: int
    student: Student
    dateCreated: datetime.datetime
    url: str
    state: STATE
    rejectionReason: REJECTION_REASON
    rejectionDescription: str

    def __init__(self, student: Student, dateCreated: datetime.datetime, url: str, state: STATE, idSelfie: int, rejectionReason: REJECTION_REASON, rejectionDescription: str):
        self.student = student

        if (dateCreated == None and type(dateCreated) != datetime.datetime):
            raise EntityError('dateCreated')
        self.dateCreated = dateCreated

        if (url == None):
            raise EntityError('url')
        self.url = url

        if (state == None or type(state) != STATE):
            raise EntityError('state')
        self.state = state

        if idSelfie == None or type(idSelfie) != int:
            raise EntityError('id')
        self.idSelfie = idSelfie

        if (rejectionReason == None or type(rejectionReason) != REJECTION_REASON):
            raise EntityError('rejectionReason')
        self.rejectionReason = rejectionReason

        if (type(rejectionDescription) != str and rejectionDescription != None):
            raise EntityError('rejectionDescription')
        self.rejectionDescription = rejectionDescription

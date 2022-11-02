import abc
import datetime
import re
from src.shared.domain.entities.student import Student
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.domain.entities.automatic_review import AutomaticReview

class Selfie(abc.ABC):
    idSelfie: int
    student: Student
    dateCreated: datetime.datetime
    url: str
    state: STATE
    rejectionReason: REJECTION_REASON
    rejectionDescription: str
    automaticReview: AutomaticReview

    def __init__(self, student: Student, dateCreated: datetime.datetime, url: str, state: STATE, idSelfie: int, rejectionReason: REJECTION_REASON, rejectionDescription: str, automaticReview: AutomaticReview):
        self.student = student

        if (dateCreated == None and type(dateCreated) != datetime.datetime):
            raise EntityError('dateCreated')
        self.dateCreated = dateCreated

        if not Selfie.validate_url(url=url):
            raise EntityError('url')
        self.url = url

        if (state == None or type(state) != STATE):
            raise EntityError('state')
        self.state = state

        if idSelfie == None or type(idSelfie) != int:
            raise EntityError('id')

        if idSelfie < 0:
            raise EntityError('id')
        
        self.idSelfie = idSelfie

        if (rejectionReason == None or type(rejectionReason) != REJECTION_REASON):
            raise EntityError('rejectionReason')
        self.rejectionReason = rejectionReason

        if (type(rejectionDescription) != str and rejectionDescription != None):
            raise EntityError('rejectionDescription')
        self.rejectionDescription = rejectionDescription
        
        if (type(automaticReview) != AutomaticReview):
            raise EntityError('automaticReview')
        self.automaticReview = automaticReview

    @staticmethod
    def validate_url(url:str) -> bool:

        if url is None:
            return False
        regex = re.compile(r'https:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)')

        if(not bool(re.fullmatch(regex, url))):
            return False
        
        return True
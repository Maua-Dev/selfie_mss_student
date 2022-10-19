from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.entities.student import Student

class StudentViewModel:
    ra: str
    email: str
    name: str
    def __init__(self, student: Student):
        self.ra = student.ra
        self.email = student.email
        self.name = student.name
        
    def to_dict(self):
        return {
            "ra": self.ra,
            "email": self.email,
            "name": self.name
        }

class UpdateSelfieViewModel:
    idSelfie: int
    dateUpload: str
    url: str
    state: STATE
    rejectionReason: REJECTION_REASON
    rejectionDescription: str

    def __init__(self, selfie: Selfie):
        self.idSelfie = selfie.idSelfie
        self.dateUpload = selfie.dateUpload
        self.url = selfie.url
        self.state = selfie.state
        self.rejectionReason =  selfie.rejectionReason
        self.rejectionDescription = selfie.rejectionDescription
        self.student = StudentViewModel(student=selfie.student)

    def to_dict(self) -> dict:
        return {
            "idSelfie" : self.idSelfie,
            "dateUpload" : self.dateUpload.isoformat(),
            "url" : self.url,
            "state" : self.state.value,
            "rejectionReason": self.rejectionReason.value,
            "rejectionDescription": self.rejectionDescription,
            "student": self.student.to_dict(),
            "message": "the selfie was updated"
        }
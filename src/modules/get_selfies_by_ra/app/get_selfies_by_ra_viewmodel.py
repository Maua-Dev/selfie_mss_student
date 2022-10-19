import datetime
from typing import List
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.entities.student import Student

class StudentViewModel:
    ra: str
    name: str
    email: str
    
    def __init__(self, student: Student):
        self.ra = student.ra
        self.name = student.name
        self.email = student.email

    def to_dict(self) -> dict:
        return  {
            "ra":self.ra,
            "name":self.name,
            "email":self.email
        }

class SelfieViewModel:
    idSelfie: int
    dateUpload: datetime.datetime
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

    def to_dict(self) -> dict:
        return {
            "idSelfie" : self.idSelfie,
            "dateUpload" : self.dateUpload.isoformat(),
            "url" : self.url,
            "state" : self.state.value,
            "rejectionReason": self.rejectionReason.value,
            "rejectionDescription": self.rejectionDescription,
        }

class GetSelfiesByRaViewModel:
    selfies: List[SelfieViewModel] 
    student: StudentViewModel

    def __init__(self, data: List[Selfie], student: Student):
        self.selfies = [SelfieViewModel(selfie) for selfie in data]
        self.student = StudentViewModel(student)
        

    def to_dict(self) -> dict:
        return {
            "student": self.student.to_dict(),
            "selfies": [selfie.to_dict() for selfie in self.selfies],
            "message": "the selfies were retriven"
        }
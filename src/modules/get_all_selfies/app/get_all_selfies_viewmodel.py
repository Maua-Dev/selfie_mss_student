from typing import List
from src.shared.domain.entities.student import Student
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.entities.selfie import Selfie


class GetStudentViewModel:
    ra:str
    email:str
    name:str
    
    def __init__(self, student:Student):
        self.ra = student.ra
        self.name = student.name
        self.email = student.email
    
    def to_dict(self) -> dict:
        return {
            "ra":self.ra,
            "email":self.email,
            "name":self.name
        }    

class GetSelfieViewModel:
    idSelfie: int
    dateCreated: str
    url: str
    state: STATE
    rejectionReason: REJECTION_REASON
    rejectionDescription: str
    student: Student

    def __init__(self, selfie: Selfie):
        self.idSelfie = selfie.idSelfie
        self.dateCreated = selfie.dateCreated
        self.url = selfie.url
        self.state = selfie.state
        self.rejectionReason =  selfie.rejectionReason
        self.rejectionDescription = selfie.rejectionDescription
        self.student = selfie.student

    def to_dict(self) -> dict:
        return {
            "idSelfie" : self.idSelfie,
            "dateCreated" : self.dateCreated.isoformat(),
            "url" : self.url,
            "state" : self.state.value,
            "rejectionReason": self.rejectionReason.value,
            "rejectionDescription": self.rejectionDescription,
            "message": "the selfie was retriven",
            "student": GetStudentViewModel(self.student).to_dict()
        }


class GetAllSelfiesViewModel:
    all_selfies: List[GetSelfieViewModel]

    def __init__(self, all_selfies: List[Selfie]):
        self.selfies = [selfie for selfie in all_selfies]

    def to_dict(self) -> dict:
        return {
            "all_selfies": [GetSelfieViewModel(selfie).to_dict() for selfie in self.selfies],
            "message": "all selfies were retriven"
        }

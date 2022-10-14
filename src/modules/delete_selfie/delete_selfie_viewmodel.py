import datetime
from typing import List
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
    dateUpload: str
    url: str
    state: STATE

    def __init__(self, selfie: Selfie):
        self.idSelfie = selfie.idSelfie
        self.dateUpload = selfie.dateUpload
        self.url = selfie.url
        self.state = selfie.state

    def to_dict(self) -> dict:
        return {
            "idSelfie" : self.idSelfie,
            "dateUpload" : self.dateUpload.isoformat(),
            "url" : self.url,
            "state" : self.state.value
        }

class DeleteSelfieViewModel:
    selfie: SelfieViewModel 
    student: StudentViewModel

    def __init__(self, data: Selfie, student: Student):
        self.selfie = SelfieViewModel(data)
        self.student = StudentViewModel(student)

    def to_dict(self) -> dict:
        return {
            "student": self.student.to_dict(),
            "selfie": self.selfie.to_dict(),
            "message": "the selfie was deleted"
        }
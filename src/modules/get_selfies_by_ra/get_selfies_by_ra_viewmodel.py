import datetime
from typing import List
from src.domain.enums.state_enum import STATE
from src.domain.entities.selfie import Selfie
from src.domain.entities.student import Student

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
    selfieId: int
    dateUpload: str
    url: str
    state: STATE

    def __init__(self, selfie: Selfie):
        self.selfieId = selfie.selfieId
        self.dateUpload = selfie.dateUpload
        self.url = selfie.url
        self.state = selfie.state

    def to_dict(self) -> dict:
        return {
            "selfieId" : self.selfieId,
            "dateUpload" : self.dateUpload.isoformat(),
            "url" : self.url,
            "state" : self.state.value
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
            "message": "the selfie has been taken"
        }
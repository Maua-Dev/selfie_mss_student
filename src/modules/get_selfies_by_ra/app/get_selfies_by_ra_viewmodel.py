import datetime
from typing import List
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.entities.student import Student
from src.shared.domain.entities.automatic_review import AutomaticReview
from src.shared.domain.entities.label import Label

class LabelViewModel:
    name: str
    coords: dict[str, float]
    confidence: float
    parents: list[str] 
    
    def __init__(self, label:Label):
        self.name = label.name            
        self.coords = label.coords            
        self.confidence = label.confidence        
        self.parents = label.parents        

        
    def to_dict(self):
        return {
            "name": self.name,
            "coords": self.coords,
            "confidence": self.confidence,
            "parents": self.parents 
        }

class AutomaticReviewViewModel:
    automaticallyRejected: bool
    rejectionReason: REJECTION_REASON
    labels: list[LabelViewModel]
    
    def __init__(self, automaticReview:AutomaticReview):
            self.automaticallyRejected = automaticReview.automaticallyRejected
            self.rejectionReason = automaticReview.rejectionReason
            self.labels = [LabelViewModel(label) for label in automaticReview.labels]

    
    def to_dict(self):
        return {
            "automaticallyRejected": self.automaticallyRejected,    
            "rejectionReason": self.rejectionReason.value,
            "labels": [label.to_dict() for label in self.labels]
        }


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
    dateCreated: datetime.datetime
    url: str
    state: STATE
    rejectionReason: REJECTION_REASON
    rejectionDescription: str
    automaticReview: AutomaticReviewViewModel

    def __init__(self, selfie: Selfie):
        self.idSelfie = selfie.idSelfie
        self.dateCreated = selfie.dateCreated
        self.url = selfie.url
        self.state = selfie.state
        self.rejectionReason =  selfie.rejectionReason
        self.rejectionDescription = selfie.rejectionDescription
        self.automaticReview = AutomaticReviewViewModel(selfie.automaticReview)

    def to_dict(self) -> dict:
        return {
            "idSelfie" : self.idSelfie,
            "dateCreated" : self.dateCreated.isoformat(),
            "url" : self.url,
            "state" : self.state.value,
            "rejectionReason": self.rejectionReason.value,
            "rejectionDescription": self.rejectionDescription,
            "automaticReview": self.automaticReview.to_dict(),
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
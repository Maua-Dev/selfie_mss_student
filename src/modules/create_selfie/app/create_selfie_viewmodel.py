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

class CreateSelfieViewModel:
    idSelfie: int
    url: str
    dateCreated: datetime.datetime
    state: STATE
    student: StudentViewModel
    rejectionReason: REJECTION_REASON
    rejectionDescription: str
    automaticReview: AutomaticReviewViewModel

    def __init__(self, data: Selfie):
        self.idSelfie = data.idSelfie
        self.url = data.url
        self.dateCreated = data.dateCreated
        self.state = data.state
        self.student = StudentViewModel(data.student)
        self.rejectionReason = data.rejectionReason
        self.rejectionDescription = data.rejectionDescription
        self.automaticReview = AutomaticReviewViewModel(data.automaticReview)
       
        
    def to_dict(self) -> dict:
        return {
            "student": self.student.to_dict(),
            "idSelfie": self.idSelfie,
            "url": self.url,
            "dateCreated": self.dateCreated.isoformat(),
            "state": self.state.value,
            "rejectionReason": self.rejectionReason.value,
            "rejectionDescription": self.rejectionDescription,
            "automaticReview": self.automaticReview.to_dict(),
            "message": "the selfie was created"
        }
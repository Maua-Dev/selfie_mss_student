from typing import List, Dict
from src.shared.domain.entities.student import Student
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.enums.student_state_enum import STUDENT_STATE
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
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
    rejectionReasons: list[REJECTION_REASON]
    labels: list[LabelViewModel]
    
    def __init__(self, automaticReview:AutomaticReview):
            self.automaticallyRejected = automaticReview.automaticallyRejected
            self.rejectionReasons = automaticReview.rejectionReasons
            self.labels = [LabelViewModel(label) for label in automaticReview.labels]

    
    def to_dict(self):
        return {
            "automaticallyRejected": self.automaticallyRejected,    
            "rejectionReasons": [reason.value for reason in self.rejectionReasons],
            "labels": [label.to_dict() for label in self.labels]
        }
        
class SelfieViewModel:
    idSelfie: int
    dateCreated: str
    url: str
    state: STATE
    rejectionReasons: list[REJECTION_REASON]
    rejectionDescription: str
    automaticReview: AutomaticReviewViewModel

    def __init__(self, selfie: Selfie):
        self.idSelfie = selfie.idSelfie
        self.dateCreated = selfie.dateCreated
        self.url = selfie.url
        self.state = selfie.state
        self.rejectionReasons =  selfie.rejectionReasons
        self.rejectionDescription = selfie.rejectionDescription
        self.automaticReview = AutomaticReviewViewModel(selfie.automaticReview)

    def to_dict(self) -> dict:
        return {
            "idSelfie" : self.idSelfie,
            "dateCreated" : self.dateCreated.isoformat(),
            "url" : self.url,
            "state" : self.state.value,
            "rejectionReasons": [reason.value for reason in self.rejectionReasons],
            "automaticReview": self.automaticReview.to_dict(),
            "rejectionDescription": self.rejectionDescription,
        }


class StudentViewModel:
    email:str
    name:str
    selfies: List[Selfie]
    status: STUDENT_STATE
    
    def __init__(self, student:Dict):
        self.name = student["name"]
        self.selfies = student["selfies"]
        self.email = student["email"]
        self.status = student["status"]
        
    
    def to_dict(self) -> dict:
        return {
            "name":self.name,
            "email":self.email,
            "status":self.status.value,
            "selfies":[SelfieViewModel(selfie).to_dict() for selfie in self.selfies]
        }    

class GetAllStudentsViewModel:
    students: List[Dict]

    def __init__(self, students: List[Dict]):
        self.students = students

    def to_dict(self) -> dict:
        return {
            "all_students": dict(zip([student["ra"] for student in self.students], [StudentViewModel(student).to_dict() for student in self.students])),
            "message": "the students were retriven"
        }

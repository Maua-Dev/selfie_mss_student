from typing import List, Dict
from src.shared.domain.entities.student import Student
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.enums.student_state_enum import STUDENT_STATE
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON

class SelfieViewModel:
    idSelfie: int
    dateCreated: str
    url: str
    state: STATE
    rejectionReason: REJECTION_REASON
    rejectionDescription: str

    def __init__(self, selfie: Selfie):
        self.idSelfie = selfie.idSelfie
        self.dateCreated = selfie.dateCreated
        self.url = selfie.url
        self.state = selfie.state
        self.rejectionReason =  selfie.rejectionReason
        self.rejectionDescription = selfie.rejectionDescription

    def to_dict(self) -> dict:
        return {
            "idSelfie" : self.idSelfie,
            "dateCreated" : self.dateCreated.isoformat(),
            "url" : self.url,
            "state" : self.state.value,
            "rejectionReason": self.rejectionReason.value,
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

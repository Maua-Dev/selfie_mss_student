from src.shared.domain.enums.review_state_enum import REVIEW_STATE
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.entities.automatic_review import AutomaticReview
from src.shared.domain.entities.label import Label
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.entities.student import Student
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.entities.review import Review
from src.shared.domain.entities.reviewer import Reviewer
import datetime


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

        
    def to_dict(self) -> dict:
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

    
    def to_dict(self) -> dict:
        return {
            "automaticallyRejected": self.automaticallyRejected,    
            "rejectionReasons": [reason.value for reason in self.rejectionReasons],
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
        return {
            "ra":self.ra,
            "email":self.email,
            "name":self.name,
        }   
         
class ReviewerViewModel:
    ra: str
    name: str
    email: str
    active: bool
    
    def __init__(self, reviewer: Reviewer):
        self.ra = reviewer.ra
        self.name = reviewer.name
        self.email = reviewer.email
        self.active = reviewer.active
        
    def to_dict(self) -> dict:
        return {
            "ra": self.ra,
            "name": self.name,
            "email": self.email,
            "active": self.active
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
            "rejectionReasons": [reason.value for reason in self.rejectionReasons] if len(self.rejectionReasons) != 0 else [],
            "rejectionDescription": self.rejectionDescription,
            "automaticReview": self.automaticReview.to_dict(),
        }
        
class RejectSelfieViewModel:
    idReview: int
    state: REVIEW_STATE
    reviewer: ReviewerViewModel
    selfie: SelfieViewModel
    dateAssigned: datetime.datetime
    dateReviewed: datetime.datetime
    
    def __init__(self, review:Review):
        self.idReview = review.idReview
        self.state = review.state
        self.reviewer = ReviewerViewModel(reviewer=review.reviewer)
        self.selfie = SelfieViewModel(selfie=review.selfie)
        self.dateAssigned = review.dateAssigned.isoformat()
        self.dateReviewed = review.dateReviewed.isoformat()
    
    def to_dict(self) -> dict:
        return {
            "idReview": self.idReview,
            "state": self.state.value,
            "reviewer": self.reviewer.to_dict(),
            "selfie": self.selfie.to_dict(),
            "dateAssigned": self.dateAssigned,
            "dateReviewed": self.dateReviewed,
            "message": "the review was rejected"
        }
        
        
        
        
        
        
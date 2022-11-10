from typing import List
from src.shared.domain.entities.automatic_review import AutomaticReview
from src.shared.domain.entities.label import Label
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON

class LabelViewModel:
    name: str
    coords: dict
    confidence: float
    parents: List[str]
    
    def __init__(self, label: Label):
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

class ValidateSelfieViewModel:
    automaticallyRejected: bool
    rejectionReasons: List[REJECTION_REASON]
    labels: List[Label]
    
    def __init__(self, data: AutomaticReview):
        self.automaticallyRejected = data.automaticallyRejected
        self.rejectionReasons = data.rejectionReasons
        self.labels = data.labels
        
    def to_dict(self) -> dict:
        return {
            "automaticallyRejected": self.automaticallyRejected,
            "rejectionReasons": self.rejectionReasons,
            "labels": [LabelViewModel(label=label).to_dict() for label in self.labels]
        }
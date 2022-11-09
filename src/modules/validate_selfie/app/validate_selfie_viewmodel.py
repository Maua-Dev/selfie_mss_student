from typing import List

class ValidateSelfieViewModel:
    automaticallyRejected: bool
    rejectionReasons: List[dict]
    labels: List[dict]
    
    def __init__(self, data: dict):
        self.automaticallyRejected = data["automaticallyRejected"]
        self.rejectionReasons = data["rejectionReasons"]
        self.labels = data["labels"]
        
    def to_dict(self) -> dict:
        return {
            "automaticallyRejected": self.automaticallyRejected,
            "rejectionReasons": self.rejectionReasons,
            "labels": self.labels
        }
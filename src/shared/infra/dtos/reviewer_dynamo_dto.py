from src.shared.domain.entities.reviewer import Reviewer

class ReviewerDynamoDTO:
    ra: str
    name: str
    email: str
    active: bool
    
    def __init__(self, ra: str, name: str, email: str, active: bool):
        self.ra = ra
        self.name = name
        self.email = email
        self.active = active

    @staticmethod
    def from_entity(reviewer: Reviewer) -> "ReviewerDynamoDTO":
        return ReviewerDynamoDTO(
            ra=reviewer.ra,
            name=reviewer.name,
            email=reviewer.email,
            active=reviewer.active
        )
        
    def to_dynamo(self) -> dict:
        return {
            "entity": "reviewer",
            "name": self.name,
            "ra": self.ra,
            "email": self.email,
            "active": self.active
        }
    
    @staticmethod
    def from_dynamo(reviewer_data: dict) -> "ReviewerDynamoDTO":
        return ReviewerDynamoDTO(
            ra=reviewer_data["ra"],
            name=reviewer_data["name"],
            email=reviewer_data["email"],
            active=reviewer_data["active"]
        )
    
    def to_entity(self) -> Reviewer:
        return Reviewer(
            ra=self.ra,
            name=self.name,
            email=self.email,
            active=self.active,
        )
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
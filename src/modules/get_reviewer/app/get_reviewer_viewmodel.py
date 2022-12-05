from src.shared.domain.entities.reviewer import Reviewer


class GetReviewerViewModel:
    ra:str
    email:str
    name:str
    active: bool
    
    def __init__(self, data:Reviewer):
        self.ra = data.ra
        self.name = data.name
        self.email = data.email
        self.active = data.active
    
    def to_dict(self) -> dict:
        return {
            "ra":self.ra,
            "email":self.email,
            "name":self.name,
            "active":self.active,
            "message": "reviewer was retrieved"
        }    
        
    

        
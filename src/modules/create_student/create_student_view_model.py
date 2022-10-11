from src.domain.entities.student import Student


class CreateStudentViewModel():

    def __init__(self, data:Student):
        self.ra = data.ra
        self.name = data.name
        self.email = data.email
    
    def to_dict(self) -> dict:
        return {
            "ra":self.ra,
            "email":self.email,
            "name":self.name,
            "message":"User was created successfully"
        }    
        
    

        
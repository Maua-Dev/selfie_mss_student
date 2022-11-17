from src.shared.domain.entities.student import Student
from src.shared.domain.enums.student_state_enum import STUDENT_STATE


class GetStudentViewModel:
    ra:str
    email:str
    name:str
    student_state:STUDENT_STATE
    
    def __init__(self, data:Student, student_state: STUDENT_STATE):
        self.ra = data.ra
        self.name = data.name
        self.email = data.email
        self.student_state = student_state
    
    def to_dict(self) -> dict:
        return {
            "ra":self.ra,
            "email":self.email,
            "name":self.name,
            "status":self.student_state.value
        }    
        
    

        
import datetime
from typing import List
from src.domain.entities.selfie import Selfie
from src.domain.entities.student import Student

class SelfiesViewModel:
    selfieId: int
    student: Student
    dateUpload: datetime.datetime
    url: str
    state: STATE


class GetSelfieByRaViewModel:
    selfies: List[] 
        
    def __init__(self, data:Student):
        self.selfies = []
    
    def to_dict(self) -> dict:
        return self.selfies
        
    

        
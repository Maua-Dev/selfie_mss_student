from abc import ABC
from typing import List, Tuple
from src.domain.entities.student import Student
from src.domain.entities.selfie import Selfie

class IStudentRepository(ABC):

    def get_student(self, ra: str) -> Student:
        pass

    def update_student(self, ra: str, new_name: str = None, new_email: str = None) -> Student:
        pass

    def delete_student(self, ra: str) -> Student:
        pass
    
    def create_student(self, student: Student) -> Student:
        pass

    def get_selfies_by_ra(self, ra: str) -> Tuple[List[Selfie], Student]:
        pass
    
    def get_selfie(self, ra: str, idSelfie: int) -> Selfie:
        pass
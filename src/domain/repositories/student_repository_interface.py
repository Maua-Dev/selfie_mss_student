from abc import ABC, abstractmethod
from typing import List, Tuple
from src.domain.entities.student import Student


class IStudentRepository(ABC):

    def get_student(self, ra: str) -> Student:
        pass

    def update_student(self, ra: str, new_name: str = None, new_email: str = None) -> None:
        pass

    def delete_student(self, ra: str) -> Student:
        pass
    
    def create_student(self, student: Student) -> Student:
        pass

    def get_students_by_ra_or_email(self, ra: str = None, email: str = None) -> List[Student]:
        pass
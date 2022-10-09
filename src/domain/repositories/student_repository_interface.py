from abc import ABC, abstractmethod
from typing import List, Tuple
from src.domain.entities.student import Student


class IStudentRepository(ABC):

    def get_student(self, ra: str, email: str) -> Student:
        pass

    def update_student(self, ra: str, new_name: str = None, new_email: str = None) -> None:
        pass
    
    def create_student(self, ra: str, name: str, email: str) -> None:
        pass
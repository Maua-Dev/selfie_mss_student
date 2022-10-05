from abc import ABC, abstractmethod
from typing import List, Tuple
from src.domain.entities.student import Student


class IStudentRepository(ABC):
    
    def get_student(self, ra:str, email:str) -> Student:
        pass

    
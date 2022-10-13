from abc import ABC, abstractmethod
from typing import List, Tuple
from src.domain.entities.student import Student
from src.domain.entities.selfie import Selfie

class IStudentRepository(ABC):

    @abstractmethod
    def get_student(self, ra: str) -> Student:
        pass

    @abstractmethod    
    def update_student(self, ra: str, new_name: str = None, new_email: str = None) -> Student:
        pass

    @abstractmethod    
    def delete_student(self, ra: str) -> Student:
        pass
    
    @abstractmethod    
    def create_student(self, student: Student) -> Student:
        pass

    @abstractmethod    
    def get_selfies_by_ra(self, ra: str) -> Tuple[List[Selfie], Student]:
        pass

    @abstractmethod    
    def get_selfie(self, ra: str, idSelfie: int) -> Selfie:
        pass
    
    @abstractmethod    
    def delete_selfie(self, ra: str, idSelfie: int) -> Tuple[Selfie, Student]:
        pass
    
    @abstractmethod    
    def delete_selfie(self, ra: str, idSelfie: int) -> Tuple[Selfie, Student]:
        pass
    
    @abstractmethod    
    def create_selfie(self, ra: str, url: str) -> Selfie:
        pass
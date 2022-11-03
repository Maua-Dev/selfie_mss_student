from abc import ABC, abstractmethod
from typing import Dict, List, Tuple
from src.shared.domain.entities.student import Student
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE

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
        """
        If selfie does not exist, then return None, None
        """

        pass
    
    @abstractmethod    
    def delete_selfie(self, ra: str, idSelfie: int) -> Tuple[Selfie, Student]:
        pass
    
    @abstractmethod    
    def create_selfie(self, selfie: Selfie) -> Selfie:
        pass
    
    @abstractmethod    
    def update_selfie(self, ra: str, idSelfie: int, new_state: STATE = None, new_rejectionReasons: REJECTION_REASON = None, new_rejectionDescription: str = None) -> Selfie:
        pass
       
    @abstractmethod    
    def get_all_selfies(self) -> List[Selfie]:
        pass
    
    @abstractmethod    
    def check_student_has_approved_selfie(self, ra: str) -> bool:
        pass
    
    @abstractmethod    
    def get_all_students(self) -> List[Student]:
        pass
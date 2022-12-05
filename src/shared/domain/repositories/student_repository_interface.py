from abc import ABC, abstractmethod
from typing import Dict, List, Tuple
from src.shared.domain.entities.reviewer import Reviewer
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
        """
        If student does not exist, then raise NoItemsFound
        """
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
    def create_selfie(self, selfie: Selfie) -> Selfie:
        pass
    
    @abstractmethod    
    def update_selfie(self, ra: str, idSelfie: int, new_state: STATE = None, new_rejectionReasons: list[REJECTION_REASON] = None, new_rejectionDescription: str = None) -> Selfie:
        pass
       
    @abstractmethod    
    def get_all_selfies(self) -> List[Selfie]:
        pass
    
    @abstractmethod    
    def check_student_has_approved_selfie(self, ra: str) -> bool:
        pass
    
    @abstractmethod    
    def get_all_students(self) -> List[Tuple[List[Selfie], Student]]:
        pass

    @abstractmethod
    def create_reviewer(self, reviwer: Reviewer) -> Reviewer:
        pass

    @abstractmethod
    def update_reviewer(self, ra: str, new_name: str = None, new_email: str = None, new_active: bool = None) -> Reviewer:
        pass

    @abstractmethod
    def delete_reviewer(self, ra: str) -> Reviewer:
        pass

    @abstractmethod
    def get_reviewer(self, ra: str) -> Reviewer:
        pass

    @abstractmethod
    def get_rejected_selfies_by_reviewer(self, reviewer_ra: str) -> List[Selfie]:
        """
        If reviewer does not exist, then raise NoItemsFound
        """
        pass
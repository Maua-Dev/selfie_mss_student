from abc import ABC, abstractmethod
from typing import Dict, List, Tuple
from src.shared.domain.entities.review import Review
from src.shared.domain.entities.reviewer import Reviewer
from src.shared.domain.entities.student import Student
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.entities.review import Review
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.enums.review_state_enum import REVIEW_STATE
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
        """
        Sorted by Selfie.dateCreated
        """
        pass
    
    @abstractmethod    
    def check_student_has_approved_selfie(self, ra: str) -> bool:
        pass
    
    @abstractmethod    
    def get_all_students(self) -> List[Tuple[List[Selfie], Student]]:
        pass
    
    @abstractmethod    
    def get_review(self, idReview: int, idSelfie:int, studentRa:str) -> Review:
        pass

    @abstractmethod    
    def create_review(self, review: Review) -> Review:
        pass
    
    @abstractmethod
    def update_review(self, reviewerRa: str, idReview: int, idSelfie:int, studentRa:str, new_state: REVIEW_STATE = None, new_rejectionReasons: List[REJECTION_REASON] = None, new_rejectionDescription: str = None) -> Review:
        """
        1°: Instanciate review.state with new_state (if new_state != None)
        2°: Update selfie in repo
        3°: Instanciate review.dateReviewed with datetime.now()
        """
        
        pass
    
    @abstractmethod
    def delete_review(self, reviewerRa: str, idReview: int, idSelfie:int, studentRa:str) -> Review:
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
    def get_rejected_reviews_by_reviewer(self, reviewerRa: str) -> Tuple[Reviewer, List[Review]]:
        """
        If reviewer does not exist, then raise NoItemsFound
        """
        pass

    @abstractmethod
    def get_approved_selfies_by_reviewer(self, reviewerRa: str) -> Tuple[Reviewer, List[Review]]:
        """
        If reviewer does not exist, then raise NoItemsFound
        """
        pass
    
    @abstractmethod
    def get_pending_validation_selfies_assigned(self, reviewerRa: str) -> List[Review]:
        pass
    
    @abstractmethod
    def assign_selfies(self, reviewerRa: str, nSelfies: int) -> List[Review]:
        pass
    
    @abstractmethod
    def get_selfies_to_review(self, reviewerRa: str, nSelfies: int = 10) -> Tuple[List[Selfie], Reviewer]:
        pass
    
    def approve_selfie(self, studentRa: str, idSelfie: int, idReview: int) -> Review:
        
        pass
    
    @abstractmethod
    def reject_selfie(self, studentRa: str, idSelfie: int, idReview: int, new_rejectionReasons: list[REJECTION_REASON] = None, new_rejectionDescription: str = None) -> Review:
        pass


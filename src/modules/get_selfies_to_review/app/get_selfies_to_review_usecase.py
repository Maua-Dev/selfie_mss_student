from typing import List
from src.shared.domain.entities.review import Review
from src.shared.domain.repositories.student_repository_interface import IStudentRepository
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.entities.student import Student
from src.shared.helpers.errors.domain_errors import EntityError


class GetSelfiesToReviewUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, reviewerRa: str, nSelfies: int = 10) -> List[Review]:
        if not Student.validate_ra(ra=reviewerRa):
            raise EntityError('reviewerRa')
        return self.repo.get_selfies_to_review(reviewerRa=reviewerRa, nSelfies=nSelfies)
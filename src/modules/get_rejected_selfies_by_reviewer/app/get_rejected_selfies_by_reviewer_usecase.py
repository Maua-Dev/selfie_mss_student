

from typing import List
from src.shared.domain.entities.reviewer import Reviewer
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.repositories.student_repository_interface import IStudentRepository
from src.shared.helpers.errors.domain_errors import EntityError


class GetRejectedSelfiesByReviewerUsecase:

    def __init__(self, repo: IStudentRepository):
        self.repo = repo

    def __call__(self, reviewerRa: str) -> List[Selfie]:

        if not Reviewer.validate_ra(reviewerRa):
            raise EntityError('ra')
        
        selfies  = self.repo.get_rejected_selfies_by_reviewer(reviewerRa)
        return selfies
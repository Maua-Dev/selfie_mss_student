from typing import List, Tuple
from src.shared.domain.entities.review import Review
from src.shared.domain.entities.reviewer import Reviewer
from src.shared.domain.repositories.student_repository_interface import IStudentRepository
from src.shared.helpers.errors.domain_errors import EntityError


class GetApprovedSelfiesByReviewerUsecase:

    def __init__(self, repo: IStudentRepository):
        self.repo = repo

    def __call__(self, reviewerRa: str) -> Tuple[Reviewer, List[Review]]:

        if not Reviewer.validate_ra(reviewerRa):
            raise EntityError('reviewerRa')
        
        reviewer, reviews  = self.repo.get_approved_selfies_by_reviewer(reviewerRa)

        return reviewer, reviews
from src.shared.domain.enums.review_state_enum import REVIEW_STATE
from src.shared.domain.repositories.student_repository_interface import IStudentRepository
from src.shared.domain.entities.review import Review
from src.shared.domain.entities.reviewer import Reviewer
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.domain.entities.student import Student

class ApproveSelfieUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, reviewerRa: str, studentRa: str, idSelfie: int, idReview: int) -> Review:
        if not Reviewer.validate_ra(ra=reviewerRa):
            raise EntityError("reviewerRa")
        if not Student.validate_ra(ra=studentRa):
            raise EntityError("studentRa")
        
        review_before = self.repo.get_review(idReview=idReview, idSelfie=idSelfie, studentRa=studentRa, reviewerRa=reviewerRa)
        if review_before == None:
            raise NoItemsFound("reviewerRa, idReview, idSelfie or studentRa")
        if review_before.state != REVIEW_STATE.PENDING_VALIDATION:
            raise ForbiddenAction("Review")
        
        review = self.repo.approve_selfie(idReview=idReview, idSelfie=idSelfie, studentRa=studentRa, reviewerRa=reviewerRa)
        
        
        
        
        return review
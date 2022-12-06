from src.shared.domain.repositories.student_repository_interface import IStudentRepository
from src.shared.domain.entities.review import Review
from src.shared.domain.entities.reviewer import Reviewer
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.domain.entities.student import Student


class GetReviewUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, reviewerRa: str, idReview: int, idSelfie: int, studentRa: str) -> Review:
        if not Reviewer.validate_ra(ra=reviewerRa):
            raise EntityError("reviewerRa")
        if not Student.validate_ra(ra=studentRa):
            raise EntityError("studentRa")
        
        
        review = self.repo.get_review(reviewerRa=reviewerRa, idReview=idReview, idSelfie=idSelfie, studentRa=studentRa)
        
        if review == None:
            raise NoItemsFound("reviewerRa, idReview, idSelfie or studentRa")
        
        return review
        
        
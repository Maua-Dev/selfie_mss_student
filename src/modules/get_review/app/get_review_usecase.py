from src.shared.domain.repositories.student_repository_interface import IStudentRepository
from src.shared.domain.entities.review import Review
from src.shared.domain.entities.reviewer import Reviewer
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound

class GetReviewUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, reviewerRa: str, idReview: str) -> Review:
        if not Reviewer.validate_ra(ra=reviewerRa):
            raise EntityError("reviewerRa")
        
        review = self.repo.get_review(reviewerRa=reviewerRa, idReview=idReview)
        
        if review == None:
            raise NoItemsFound("reviewerRa or idReview")
        
        return review
        
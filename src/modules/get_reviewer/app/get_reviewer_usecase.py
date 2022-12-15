from src.shared.domain.entities.reviewer import Reviewer
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.domain.repositories.student_repository_interface import IStudentRepository

class GetReviewerUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, ra: str) -> Reviewer:

      if not Reviewer.validate_ra(ra):
          raise EntityError('ra')

      reviewer = self.repo.get_reviewer(ra=ra)

      if reviewer == None:
          raise NoItemsFound("Reviewer")

      return reviewer

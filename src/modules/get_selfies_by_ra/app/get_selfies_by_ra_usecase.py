from typing import List, Tuple
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.domain.entities.student import Student
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.repositories.student_repository_interface import IStudentRepository
class GetSelfiesByRaUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, ra: str) -> Tuple[List[Selfie], Student]:

        if not Student.validate_ra(ra):
            raise EntityError('ra')

        selfies, student = self.repo.get_selfies_by_ra(ra=ra)
     
        return selfies, student
        
        
from typing import List
from src.helpers.errors.domain_errors import EntityError
from src.helpers.errors.usecase_errors import NoItemsFound
from src.domain.entities.student import Student
from src.domain.entities.selfie import Selfie
from src.domain.repositories.student_repository_interface import IStudentRepository
class GetSelfiesByRaUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, ra: str) -> List[Selfie]:

        if not Student.validate_ra(ra):
            raise EntityError('ra')

        if self.repo.get_student(ra=ra) ==  None:
            raise NoItemsFound("ra")
   
        selfies = self.repo.get_selfies_by_ra(ra=ra)
     
        return selfies
        
        
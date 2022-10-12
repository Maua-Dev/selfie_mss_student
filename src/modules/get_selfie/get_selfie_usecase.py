from typing import List, Tuple
from src.helpers.errors.domain_errors import EntityError
from src.helpers.errors.usecase_errors import NoItemsFound
from src.domain.entities.student import Student
from src.domain.entities.selfie import Selfie
from src.domain.repositories.student_repository_interface import IStudentRepository
class GetSelfieUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, ra: str, idSelfie: int) -> Selfie:

        if not Student.validate_ra(ra):
            raise EntityError('ra')

        selfie = self.repo.get_selfie(ra=ra, idSelfie=idSelfie)
        
        if selfie == None:
            raise NoItemsFound("ra or idSelfie")
   
        selfie = self.repo.get_selfie(ra=ra, idSelfie=idSelfie)
     
        return selfie
        
        
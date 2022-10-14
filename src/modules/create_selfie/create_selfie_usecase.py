from re import U
from typing import Tuple
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.domain.entities.student import Student
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.repositories.student_repository_interface import IStudentRepository
class CreateSelfieUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, ra: str, url: str) -> Selfie:

        if not Student.validate_ra(ra):
            raise EntityError('ra')

        selfie = self.repo.create_selfie(ra=ra, url=url)
        if selfie.student == None:
            raise NoItemsFound("ra")
        
        return selfie
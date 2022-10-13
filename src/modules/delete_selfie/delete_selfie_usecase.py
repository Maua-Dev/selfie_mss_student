from typing import Tuple
from src.domain.entities.selfie import Selfie
from src.helpers.errors.domain_errors import EntityError
from src.helpers.errors.usecase_errors import NoItemsFound
from src.domain.entities.student import Student
from src.infra.repositories.student_repository_mock import IStudentRepository

class DeleteSelfieUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, ra: str, idSelfie: int) -> Tuple[Selfie, Student]:
        
        if not Student.validate_ra(ra):
            raise EntityError('ra')

        selfie, student = self.repo.delete_selfie(ra=ra, idSelfie=idSelfie)

        if student == None:
            raise NoItemsFound('ra or idSelfie')

        return selfie, student
        
from typing import Tuple
from src.shared.domain.entities.selfie import Selfie
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.domain.entities.student import Student
from src.shared.infra.repositories.student_repository_mock import IStudentRepository

class DeleteSelfieUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, ra: str, idSelfie: int) -> Tuple[Selfie, Student]:
        
        if not Student.validate_ra(ra):
            raise EntityError('ra')
    
        if self.repo.check_student_has_approved_selfie(ra=ra):       
            raise ForbiddenAction("Selfie")

        selfie, student = self.repo.delete_selfie(ra=ra, idSelfie=idSelfie)

        if student == None:
            raise NoItemsFound('ra or idSelfie')

        return selfie, student
        
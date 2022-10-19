from src.shared.domain.repositories.student_repository_interface import IStudentRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.entities.student import Student
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE



class UpdateSelfieUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, ra: str, idSelfie: int, new_state: STATE = None, new_rejectionReason: REJECTION_REASON = None, new_rejectionDescription = None) -> Student:
        if not Student.validate_ra(ra):
            raise EntityError('ra')

        if idSelfie == None or type(idSelfie) != int:
            raise EntityError('id')

        return self.repo.update_selfie(ra=ra, idSelfie=idSelfie, new_state=new_state, new_rejectionReason=new_rejectionReason, new_rejectionDescription=new_rejectionDescription)
        
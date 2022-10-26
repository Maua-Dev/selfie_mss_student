import datetime
import re
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ForbiddenAction
from src.shared.domain.entities.student import Student
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.repositories.student_repository_interface import IStudentRepository
class CreateSelfieUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, ra: str, url: str) -> Selfie:
        
        if not Student.validate_ra(ra):
            raise EntityError('ra')
        
        student = self.repo.get_student(ra=ra)
        if student == None:
            raise NoItemsFound("ra")
        
        if self.repo.check_student_has_approved_selfie(ra=ra):       
            raise ForbiddenAction("Student")
             
        selfie = Selfie(
            student=student,
            dateCreated=datetime.datetime.now(),
            url=url,
            state=STATE.PENDING_REVIEW,
            idSelfie=len(self.repo.get_selfies_by_ra(ra=ra)),
            rejectionReason=REJECTION_REASON.NONE,
            rejectionDescription=None
        )
        
        selfie = self.repo.create_selfie(selfie=selfie)
        
        return selfie
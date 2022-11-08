from typing import Tuple
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.enums.student_state_enum import STUDENT_STATE
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.domain.entities.student import Student
from src.shared.domain.repositories.student_repository_interface import IStudentRepository
from src.shared.helpers.errors.domain_errors import EntityParameterError

class GetStudentUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, ra: str) -> Tuple[Student, STUDENT_STATE]:


        if not Student.validate_ra(ra):
            raise EntityError('ra')

        student = self.repo.get_student(ra=ra)

        if student == None:
            raise NoItemsFound("Student")

        selfies = self.repo.get_selfies_by_ra(ra=student.ra)
        
        if not len(selfies): student_state = STUDENT_STATE.NO_SELFIE
        elif self.repo.check_student_has_approved_selfie(ra=student.ra): student_state = STUDENT_STATE.APPROVED
        else:
            selfies.sort(key=lambda x:x.dateCreated)
            recent_selfie_status = selfies[-1].state 
            if recent_selfie_status == STATE.DECLINED: student_state = STUDENT_STATE.SELFIE_REJECTED
            elif recent_selfie_status == STATE.IN_REVIEW: student_state = STUDENT_STATE.SELFIE_IN_REVIEW
            elif recent_selfie_status == STATE.PENDING_REVIEW: student_state = STUDENT_STATE.SELFIE_PENDING_REVIEW
            else: raise EntityParameterError(message=f"state {recent_selfie_status.value} is unknown")

        
        return student, student_state
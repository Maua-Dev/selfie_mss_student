from typing import Dict, List
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.entities.student import Student
from src.shared.domain.repositories.student_repository_interface import IStudentRepository
from src.shared.domain.enums.student_state_enum import STUDENT_STATE
from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.domain_errors import EntityParameterError

class GetAllStudentsUsecase:
      def __init__(self, repo:IStudentRepository):
        self.repo = repo
  
      def __call__(self) -> List[Dict]:

        all_students_list = list()
        
        for student in self.repo.get_all_students():
            student_dict = dict()
            
            selfies = self.repo.get_selfies_by_ra(ra=student.ra)
            
            if len(selfies) == 0: status = STUDENT_STATE.NO_SELFIE
            elif self.repo.check_student_has_approved_selfie(ra=student.ra): status = STUDENT_STATE.APPROVED
            else:
                selfies.sort(key=lambda x:x.dateCreated)
                recent_selfie_status = selfies[-1].state 
                if recent_selfie_status == STATE.DECLINED: status = STUDENT_STATE.SELFIE_REJECTED
                elif recent_selfie_status == STATE.IN_REVIEW: status = STUDENT_STATE.SELFIE_IN_REVIEW
                elif recent_selfie_status == STATE.PENDING_REVIEW: status = STUDENT_STATE.SELFIE_PENDING_REVIEW
                else: raise EntityParameterError(message=f"state {recent_selfie_status.value} is unknown")
            
            student_dict["ra"] = student.ra
            student_dict["name"] = student.name
            student_dict["email"] = student.email
            student_dict["selfies"] = selfies
            student_dict["status"] = status
            
            all_students_list.append(student_dict)
            
        return all_students_list
            
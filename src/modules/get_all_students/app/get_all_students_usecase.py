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
         
        all_students = self.repo.get_all_students()
        all_selfies = self.repo.get_all_selfies()

        group_selfies_by_ra = dict()

        for student in all_students:
            group_selfies_by_ra[student.ra] =  {
                "selfies": list(),
                "student": student
            }

        group_selfies_by_ra["unknown-ra"] = {"selfies":list()}

        for selfie in all_selfies:
            if selfie.student.ra in group_selfies_by_ra.keys():
                group_selfies_by_ra[selfie.student.ra]["selfies"].append(selfie)
            else:
                if len(group_selfies_by_ra["unknown-ra"]["selfies"]) == 0:
                    group_selfies_by_ra["unknown-ra"]["student"] = selfie.student

                group_selfies_by_ra["unknown-ra"]["selfies"].append(selfie)
                
        if len(group_selfies_by_ra["unknown-ra"]["selfies"]) == 0:
            group_selfies_by_ra.pop("unknown-ra")

        for raKey in group_selfies_by_ra.keys() :
            selfies = group_selfies_by_ra[raKey]['selfies']
            student = group_selfies_by_ra[raKey]["student"]

            student_dict = dict()
            
            selfies.sort(key=lambda x: x.dateCreated)

            if len(selfies) == 0: status = STUDENT_STATE.NO_SELFIE
            elif any([selfie.state == STATE.APPROVED for selfie in selfies]): status = STUDENT_STATE.APPROVED
            else:
                recent_selfie_status = selfies[-1].state 
                if recent_selfie_status == STATE.DECLINED: status = STUDENT_STATE.SELFIE_REJECTED
                elif recent_selfie_status == STATE.IN_REVIEW: status = STUDENT_STATE.SELFIE_IN_REVIEW
                elif recent_selfie_status == STATE.PENDING_REVIEW: status = STUDENT_STATE.SELFIE_PENDING_REVIEW
                else: raise EntityParameterError(message=f"state {recent_selfie_status.value} is unknown")
            
            if raKey == "unknown-ra":
                student_dict = {
                    "ra": "unknown-ra",
                    "name": "unknown-name",
                    "email": "unknown-email"
                }
            else: 
                student_dict = {
                    "ra": student.ra,
                    "name": student.name,
                    "email": student.email
                }

            
            student_dict["selfies"] = selfies
            student_dict["status"] = status
            
            all_students_list.append(student_dict)
            
        return all_students_list
            
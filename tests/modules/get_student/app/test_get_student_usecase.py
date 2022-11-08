from src.modules.get_student.app.get_student_usecase import GetStudentUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.domain.enums.student_state_enum import STUDENT_STATE
import pytest

class Test_GetStudentUsecase:
    def test_get_student_usecase(self):
         repo = StudentRepositoryMock()
         usecase = GetStudentUsecase(repo=repo)
         
         student, student_state = usecase(
            ra="21014442",
         )
         
         assert student == repo.students[1]
         assert student_state == STUDENT_STATE.SELFIE_PENDING_REVIEW
       
    def test_get_student_usecase_not_found_ra(self):
        repo = StudentRepositoryMock()
        usecase = GetStudentUsecase(repo=repo)
       

        with pytest.raises(NoItemsFound):
          usecase(
            ra="21014441",
          )
        
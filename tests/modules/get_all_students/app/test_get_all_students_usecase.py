from src.modules.get_all_students.app.get_all_students_usecase import GetAllStudentsUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.domain.enums.student_state_enum import STUDENT_STATE
import pytest

class Test_GetAllStudentsUsecase:
    def test_get_all_students(self):
        repo = StudentRepositoryMock()
        usecase = GetAllStudentsUsecase(repo=repo)
       
        all_students = usecase()
       
        assert len(all_students) == len(repo.students) 
        assert all_students[0]["name"] == "Victor"
        assert all_students[0]["status"] == STUDENT_STATE.APPROVED
        assert len(all_students[0]["selfies"]) == 2
        assert all_students[1]["status"] == STUDENT_STATE.SELFIE_PENDING_REVIEW
        assert all_students[3]["status"] == STUDENT_STATE.SELFIE_IN_REVIEW
        assert all_students[4]["status"] == STUDENT_STATE.NO_SELFIE
        assert all_students[6]["status"] == STUDENT_STATE.SELFIE_REJECTED
        
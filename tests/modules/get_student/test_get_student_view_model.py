import pytest
from src.modules.get_student.get_student_view_model import GetStudentViewModel
from src.shared.domain.entities.student import Student
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock

class Test_GetStudentViewModel:
    def test_get_student_view_model(self):
        repo = StudentRepositoryMock()
        student = repo.students[0]
        result = {
            "ra":"21010757",
            "name":"Victor",
            "email":"eusousoller@gmail.com"
        }
        
        studentViewModel = GetStudentViewModel(student).to_dict()
        
        assert studentViewModel == result
        
        
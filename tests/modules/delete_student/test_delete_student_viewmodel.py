import pytest
from src.modules.delete_student.delete_student_viewmodel import DeleteStudentViewModel
from src.domain.entities.student import Student
from src.infra.repositories.student_repository_mock import StudentRepositoryMock

class Test_DeleteStudentViewModel:
    def test_delete_student_view_model(self):
        repo = StudentRepositoryMock()
        student = repo.students[0]
        result = {
            "ra":"21010757",
            "name":"Victor",
            "email":"eusousoller@gmail.com"
        }
        
        studentViewModel = DeleteStudentViewModel(student).to_dict()
        
        assert studentViewModel == result
        
        
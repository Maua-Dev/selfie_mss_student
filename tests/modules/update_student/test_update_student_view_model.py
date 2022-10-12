import pytest
from src.modules.update_student.update_student_view_model import UpdateStudentViewModel
from src.domain.entities.student import Student
from src.infra.repositories.student_repository_mock import StudentRepositoryMock

class Test_UpdateStudentViewModel:
    def test_update_student_view_model(self):
        repo = StudentRepositoryMock()

        result = {
            "ra":"21010757",
            "name":"Vitor",
            "email":"eusousoller@gmail.com",
            "message": "User was updated successfully"
        }

        student = Student(
            ra=result["ra"],
            name=result["name"],
            email=result["email"]
        )
        
        
        studentViewModel = UpdateStudentViewModel(student=student).to_dict()
        
        assert studentViewModel == result
        
        
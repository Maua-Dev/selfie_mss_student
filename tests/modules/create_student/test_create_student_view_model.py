import pytest
from src.modules.create_student.create_student_view_model import CreateStudentViewModel
from src.domain.entities.student import Student
from src.infra.repositories.student_repository_mock import StudentRepositoryMock


class Test_CreateStudentViewModel:
    def test_create_student_view_model(self):
        repo = StudentRepositoryMock()

        student = Student(
            ra="21007586",
            name="Guilherme Clementino",
            email="gui@cleme.com"
        )

        expected = {
            "ra": "21007586",
            "name": "Guilherme Clementino",
            "email": "gui@cleme.com",
            "message": "User was created successfully"
        }

        studentViewModel = CreateStudentViewModel(student).to_dict()

        assert studentViewModel == expected

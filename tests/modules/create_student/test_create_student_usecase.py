from src.domain.entities.student import Student
from src.helpers.errors.domain_errors import EntityError
from src.modules.create_student.create_student_usecase import CreateStudentUsecase
from src.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound
import pytest


class Test_CreateStudentUsecase:
    def test_create_student_usecase(self):
        repo = StudentRepositoryMock()
        usecase = CreateStudentUsecase(repo=repo)

        studentTest = Student(
            ra="20006110", name="Ai Rubio", email="aii@rubio.com"
        )

        lenBefore = len(repo.students)

        student = usecase(studentTest)

        lenAfter = lenBefore + 1

        assert len(repo.students) == lenAfter
        assert repo.students[lenAfter - 1].ra == studentTest.ra
        assert repo.students[lenAfter - 1].name == studentTest.name
        assert repo.students[lenAfter - 1].email == studentTest.email
        assert student == studentTest

   
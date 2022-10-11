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

        student = Student(
            ra="20006110", name="Ai Rubio", email="aii@rubio.com"
        )

        usecase(student)

        assert len(repo.students) == 6
        assert repo.students[5].ra == "20006110"
        assert repo.students[5].name == "Ai Rubio"
        assert repo.students[5].email == "aii@rubio.com"

    def test_create_student_usecase_duplicated_ra(self):
        repo = StudentRepositoryMock()
        usecase = CreateStudentUsecase(repo=repo)

        student = Student(
            ra="21014442", name="Ai Rubio", email="aii@rubio.com"
        )

        with pytest.raises(DuplicatedItem):
            usecase(student)

    def test_create_student_usecase_duplicated_email(self):
        repo = StudentRepositoryMock()
        usecase = CreateStudentUsecase(repo=repo)

        student = Student(
            ra="20006110", name="Ai Rubio", email="uuaa@floresta.com"
        )

        with pytest.raises(DuplicatedItem):
            usecase(student)

from src.shared.helpers.errors.domain_errors import EntityError
from src.modules.update_student.update_student_usecase import UpdateStudentUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound
import pytest

class Test_UpdateStudentUsecase:
    def test_update_student_usecase_name(self):
        repo = StudentRepositoryMock()
        usecase = UpdateStudentUsecase(repo=repo)
        usecase(ra="21010757", new_name="Vitor")

        assert repo.students[0].name == "Vitor"

    def test_update_student_usecase_email(self):
        repo = StudentRepositoryMock()
        usecase = UpdateStudentUsecase(repo=repo)

        usecase(ra="21010757", new_email="joaovitor@outlook.com")

        assert repo.students[0].email == "joaovitor@outlook.com"

    def test_update_student_usecase_not_found_ra(self):
        repo = StudentRepositoryMock()
        usecase = UpdateStudentUsecase(repo=repo)

        with pytest.raises(NoItemsFound):
            usecase(
                ra="21014441",
            )

    def test_update_student_usecase_invalid_ra(self):
        repo = StudentRepositoryMock()
        usecase = UpdateStudentUsecase(repo=repo)

        with pytest.raises(EntityError):
            usecase(
                ra=21014441,
                new_email="joaovitor@outlook.com"
            )

 
            
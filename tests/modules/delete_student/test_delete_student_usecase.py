from src.helpers.errors.domain_errors import EntityError
from src.modules.delete_student.delete_student_usecase import DeleteStudentUsecase
from src.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.helpers.errors.usecase_errors import NoItemsFound
import pytest

class Test_DeleteStudentUsecase:
    def test_delete_student_usecase_name(self):
        repo = StudentRepositoryMock()
        usecase = DeleteStudentUsecase(repo=repo)
        usecase(ra="21010757")

        assert len(repo.students) == 4

    def test_delete_student_usecase_invalid_ra(self):
        repo = StudentRepositoryMock()
        usecase = DeleteStudentUsecase(repo=repo)

        with pytest.raises(NoItemsFound):
            usecase(
                ra="21014441",
            )

    def test_delete_student_usecase_not_found_ra(self):
        repo = StudentRepositoryMock()
        usecase = DeleteStudentUsecase(repo=repo)

        with pytest.raises(EntityError):
            usecase(
                ra=21014441,
            )

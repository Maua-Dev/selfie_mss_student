from src.shared.domain.entities.student import Student
from src.shared.helpers.errors.domain_errors import EntityError
from src.modules.delete_student.app.delete_student_usecase import DeleteStudentUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.errors.usecase_errors import NoItemsFound
import pytest

class Test_DeleteStudentUsecase:
    def test_delete_student_usecase_name(self):
        repo = StudentRepositoryMock()
        lenghtBefore = len(repo.students)
        usecase = DeleteStudentUsecase(repo=repo)
        student = usecase(ra="21010757")

        expected = Student(
            ra="21010757",
            name="Victor",
            email="eusousoller@gmail.com"   
        )

        assert len(repo.students) == lenghtBefore - 1
        assert [student.ra, student.name, student.email] == [expected.ra, expected.name, expected.email]
        

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

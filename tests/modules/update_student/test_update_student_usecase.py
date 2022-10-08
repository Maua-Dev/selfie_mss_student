from src.helpers.errors.domain_errors import EntityError
from src.modules.update_student.update_student_usecase import UpdateStudentUsecase
from src.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.helpers.errors.usecase_errors import NoItemsFound
import pytest

""""
            Student(
                ra="21010757",
                name="Victor",
                email="eusousoller@gmail.com"
            ),
            Student(
                ra="21014442",
                name="Soller",
                email="eutambemsousoler@outlook.com"
            ),
            Student(
                ra="21014443",
                name="Guirão",
                email="acreditaquesousollertambem@yahoo.com"
            ),
            Student(
                ra="21014440",
                name="Eh o Vilas do Mockas",
                email="eusouoawsboy@amazon.com"
            ),
            Student(
                ra="17090212",
                name="Monkey Guy",
                email="uuaa@floresta.com"
            )
        ]
"""


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

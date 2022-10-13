from src.domain.entities.student import Student
from src.helpers.errors.domain_errors import EntityError
from src.modules.delete_selfie.delete_selfie_usecase import DeleteSelfieUsecase
from src.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.helpers.errors.usecase_errors import NoItemsFound
import pytest

class Test_DeleteStudentUsecase:
    def test_delete_selfie_usecase_name(self):
        repo = StudentRepositoryMock()

        lenghtBefore = len(repo.selfies)
        expected = repo.selfies[0]

        usecase = DeleteSelfieUsecase(repo=repo)
        selfie, student = usecase(ra=repo.students[0].ra, idSelfie = repo.selfies[0].idSelfie)


        assert len(repo.selfies) == lenghtBefore - 1
        assert [selfie.url, selfie.dateUpload, selfie.idSelfie, selfie.state, selfie.student] == [expected.url, expected.dateUpload, expected.idSelfie, expected.state, expected.student]
        assert student == repo.students[0]
        

    def test_delete_selfie_usecase_not_found_ra(self):
        repo = StudentRepositoryMock()
        usecase = DeleteSelfieUsecase(repo=repo)

        with pytest.raises(NoItemsFound):
            usecase(
                ra="21002088",
                idSelfie=1
            )

    def test_delete_selfie_usecase_invalid_ra(self):
        repo = StudentRepositoryMock()
        usecase = DeleteSelfieUsecase(repo=repo)

        with pytest.raises(EntityError):
            usecase(
                ra=21014441,
                idSelfie=1
            )

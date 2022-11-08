from src.shared.helpers.errors.domain_errors import EntityError
from src.modules.delete_selfie.app.delete_selfie_usecase import DeleteSelfieUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
import pytest

class Test_DeleteSelfieUsecase:
    def test_delete_selfie_usecase(self):
        repo = StudentRepositoryMock()

        lenghtBefore = len(repo.selfies)
        expected = repo.selfies[2]

        usecase = DeleteSelfieUsecase(repo=repo)
        selfie, student = usecase(ra=repo.students[1].ra, idSelfie = repo.selfies[2].idSelfie)


        assert len(repo.selfies) == lenghtBefore - 1
        assert [selfie.url, selfie.dateCreated, selfie.idSelfie, selfie.state, selfie.student] == [expected.url, expected.dateCreated, expected.idSelfie, expected.state, expected.student]
        assert student == repo.students[1]
        

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

    def test_delete_selfie_usecase_no_selfie_found(self):
        repo = StudentRepositoryMock()
        usecase = DeleteSelfieUsecase(repo=repo)

        with pytest.raises(NoItemsFound):
            usecase(
                ra="21014442",
                idSelfie=10
            )

    def test_delete_selfie_forbidden_Action(self):
        repo = StudentRepositoryMock()
        usecase = DeleteSelfieUsecase(repo=repo)

        with pytest.raises(ForbiddenAction):
            usecase(
                ra="21010757",
                idSelfie=1
            )
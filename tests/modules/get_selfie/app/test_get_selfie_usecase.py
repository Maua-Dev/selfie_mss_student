from src.shared.helpers.errors.domain_errors import EntityError
from src.modules.get_selfie.app.get_selfie_usecase import GetSelfieUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.errors.usecase_errors import NoItemsFound
import pytest

class Test_GetSelfieUsecase:
    def test_get_selfie(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfieUsecase(repo=repo)
       
        selfie = usecase(ra=repo.students[0].ra, idSelfie=repo.selfies[1].idSelfie)
       
        assert selfie.idSelfie == repo.selfies[1].idSelfie

    def test_get_selfies_usecase_not_found_selfie(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfieUsecase(repo=repo)
        with pytest.raises(NoItemsFound):
            selfie = usecase(ra=repo.students[4].ra, idSelfie=1)

    def test_get_selfies_usecase_not_found_ra(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfieUsecase(repo=repo)
          
        with pytest.raises(NoItemsFound):
            selfies = usecase(ra="21002088", idSelfie=0)
          
    def test_get_selfies_usecase_invalid_ra(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfieUsecase(repo=repo)
        
        with pytest.raises(EntityError):
            selfies = usecase(ra="21.00208-8", idSelfie=0)

from src.modules.get_all_selfies.app.get_all_selfies_usecase import GetAllSelfiesUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
import pytest

class Test_GetAllSelfiesUsecase:
    def test_get_selfie(self):
        repo = StudentRepositoryMock()
        usecase = GetAllSelfiesUsecase(repo=repo)
       
        all_selfies = usecase()
       
        assert all_selfies == repo.selfies
from src.helpers.errors.domain_errors import EntityError
from src.modules.get_selfies_by_ra.get_selfies_by_ra_usecase import GetSelfiesByRaUsecase
from src.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.helpers.errors.usecase_errors import NoItemsFound
import pytest

class Test_GetSelfieByRaUsecase:
    def test_get_selfies_by_ra_usecase_1(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesByRaUsecase(repo=repo)
       
        selfies = usecase(ra="21014442")
       
        assert len(selfies) == 1
       
    def test_get_selfies_by_ra_usecase_2(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesByRaUsecase(repo=repo)
       
        selfies = usecase(ra="21010757")
       
        assert len(selfies) == 2
       
    def test_get_selfies_by_ra_usecase_not_found_selfies(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesByRaUsecase(repo=repo)
       
        assert len(usecase(ra="17090212")) == 0
    
    def test_get_selfies_by_ra_usecase_not_found_ra(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesByRaUsecase(repo=repo)
          
        with pytest.raises(NoItemsFound):
          selfies = usecase(ra="21002088")
          
    def test_get_selfies_by_ra_usecase_invalid_ra(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesByRaUsecase(repo=repo)
        
        with pytest.raises(EntityError):
            selfies = usecase(ra="21.00208-8")

from src.shared.domain.entities.student import Student
from src.shared.helpers.errors.domain_errors import EntityError
from src.modules.get_selfies_by_ra.app.get_selfies_by_ra_usecase import GetSelfiesByRaUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.errors.usecase_errors import NoItemsFound
import pytest

class Test_GetSelfieByRaUsecase:
    def test_get_selfies_by_ra_usecase_1(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesByRaUsecase(repo=repo)
       
        selfies, student = usecase(ra=repo.students[1].ra)
       
        assert len(selfies) == 1
        assert student == repo.students[1]
        
    def test_get_selfies_by_ra_usecase_2(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesByRaUsecase(repo=repo)
       
        selfies, student = usecase(ra=repo.students[0].ra)
       
        assert len(selfies) == 2
        assert student == repo.students[0]
        
    

    def test_get_selfies_by_ra_usecase_not_found_selfies(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesByRaUsecase(repo=repo)

        selfies, student = usecase(ra=repo.students[4].ra)

        assert len(selfies) == 0
        assert student == repo.students[4]
    
    def test_get_selfies_by_ra_usecase_not_found_ra(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesByRaUsecase(repo=repo)
          
        with pytest.raises(NoItemsFound):
            selfies = usecase(ra="21003068")
          
    def test_get_selfies_by_ra_usecase_invalid_ra(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesByRaUsecase(repo=repo)
        
        with pytest.raises(EntityError):
            selfies = usecase(ra="21.00208-8")

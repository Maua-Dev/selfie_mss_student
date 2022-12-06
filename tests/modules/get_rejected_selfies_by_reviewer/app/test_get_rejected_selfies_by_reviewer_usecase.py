

import pytest
from src.modules.get_rejected_selfies_by_reviewer.app.get_rejected_selfies_by_reviewer_usecase import GetRejectedSelfiesByReviewerUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock

class Test_GetRejectedSelfiesByReviewerUseCase():

    def test_get_rejected_selfies_by_reviewer(self):
        repo = StudentRepositoryMock()
        usecase = GetRejectedSelfiesByReviewerUsecase(repo=repo)
         
        selfies = usecase(
            reviewer_ra="04618"
         )
         
        assert selfies == [repo.selfies[7], repo.selfies[9]]
          
    def test_get_rejected_selfies_by_reviewer_empty_list(self):
        repo = StudentRepositoryMock()
        usecase = GetRejectedSelfiesByReviewerUsecase(repo=repo)
         
        selfies = usecase(
            reviewer_ra="04359"
         )
         
        assert selfies == []
          
    def test_get_rejected_selfies_by_reviewer_ra_not_found(self):
        repo = StudentRepositoryMock()
        usecase = GetRejectedSelfiesByReviewerUsecase(repo=repo)

        with pytest.raises(NoItemsFound): 
          selfies = usecase(
              reviewer_ra="77777"
          )
         
          
    def test_get_rejected_selfies_by_reviewer_ra_not_valid(self):
        repo = StudentRepositoryMock()
        usecase = GetRejectedSelfiesByReviewerUsecase(repo=repo)

        with pytest.raises(EntityError): 
          selfies = usecase(
              reviewer_ra="1234"
          )
         
        
          

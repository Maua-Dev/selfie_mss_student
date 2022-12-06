

import pytest
from src.modules.get_rejected_selfies_by_reviewer.app.get_rejected_selfies_by_reviewer_usecase import GetRejectedSelfiesByReviewerUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock

class Test_GetRejectedSelfiesByReviewerUseCase():

    def test_get_rejected_selfies_by_reviewer(self):
        repo = StudentRepositoryMock()
        usecase = GetRejectedSelfiesByReviewerUsecase(repo=repo)
         
        reviewer, selfies = usecase(
            reviewerRa="04618"
         )
         
        assert selfies == [repo.selfies[7], repo.selfies[9]]
        assert reviewer == repo.reviewers[3]
          
    def test_get_rejected_selfies_by_reviewer_empty_list(self):
        repo = StudentRepositoryMock()
        usecase = GetRejectedSelfiesByReviewerUsecase(repo=repo)
         
        reviewer, selfies = usecase(
            reviewerRa="04359"
         )
         
        assert selfies == []
        assert reviewer == repo.reviewers[1]
          
    def test_get_rejected_selfies_by_reviewerRa_not_found(self):
        repo = StudentRepositoryMock()
        usecase = GetRejectedSelfiesByReviewerUsecase(repo=repo)

        with pytest.raises(NoItemsFound): 
          reviewer, selfies = usecase(
              reviewerRa="77777"
          )
         
          
    def test_get_rejected_selfies_by_reviewerRa_not_valid(self):
        repo = StudentRepositoryMock()
        usecase = GetRejectedSelfiesByReviewerUsecase(repo=repo)

        with pytest.raises(EntityError): 
          reviewer, selfies = usecase(
              reviewerRa="1234"
          )
         
        
          

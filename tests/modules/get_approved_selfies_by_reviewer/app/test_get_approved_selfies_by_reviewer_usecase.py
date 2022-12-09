

import pytest
from src.modules.get_approved_selfies_by_reviewer.app.get_approved_selfies_by_reviewer_usecase import GetApprovedSelfiesByReviewerUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock

class Test_GetApprovedSelfiesByReviewerUseCase():

    def test_get_approved_selfies_by_reviewer(self):
        repo = StudentRepositoryMock()
        usecase = GetApprovedSelfiesByReviewerUsecase(repo=repo)
         
        reviewer, reviews = usecase(
            reviewerRa= repo.reviewers[0].ra
         )
         
        assert reviews == [repo.reviews[0], repo.reviews[1]]
        assert reviewer == repo.reviewers[0]
          
    def test_get_approved_selfies_by_reviewer_empty_list(self):
        repo = StudentRepositoryMock()
        usecase = GetApprovedSelfiesByReviewerUsecase(repo=repo)
         
        reviewer, reviews = usecase(
            reviewerRa= repo.reviewers[1].ra
         )
         
        assert reviews == []
        assert reviewer == repo.reviewers[1]
          
    def test_get_approved_selfies_by_reviewerRa_not_found(self):
        repo = StudentRepositoryMock()
        usecase = GetApprovedSelfiesByReviewerUsecase(repo=repo)

        with pytest.raises(NoItemsFound): 
          reviewer, reviews = usecase(
              reviewerRa="77777"
          )
         
          
    def test_get_approved_selfies_by_reviewerRa_not_valid(self):
        repo = StudentRepositoryMock()
        usecase = GetApprovedSelfiesByReviewerUsecase(repo=repo)

        with pytest.raises(EntityError): 
          reviewer, reviews = usecase(
              reviewerRa="1234"
          )
         
        
          

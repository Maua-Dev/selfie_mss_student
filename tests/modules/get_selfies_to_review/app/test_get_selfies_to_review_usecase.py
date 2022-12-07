import pytest
from src.modules.get_selfies_to_review.app.get_selfies_to_review_usecase import GetSelfiesToReviewUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.errors.domain_errors import EntityError


class Test_GetSelfiesToReviewUsecase:
    def test_get_selfies_to_review_usecase(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesToReviewUsecase(repo=repo)
        
        selfies = usecase(reviewerRa=repo.reviewers[3].ra, nSelfies=5)
        len(selfies) == 5
        
    def test_get_selfies_to_review_invalid_reviewerRa(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesToReviewUsecase(repo=repo)
        with pytest.raises(EntityError):
            selfies = usecase(reviewerRa="210202", nSelfies=2022)
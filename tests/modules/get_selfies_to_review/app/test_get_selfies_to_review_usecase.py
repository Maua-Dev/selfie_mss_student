import pytest
from src.modules.get_selfies_to_review.app.get_selfies_to_review_usecase import GetSelfiesToReviewUsecase
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.domain.entities.reviewer import Reviewer



class Test_GetSelfiesToReviewUsecase:
    def test_get_selfies_to_review_usecase(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesToReviewUsecase(repo=repo)
        
        reviews, reviewer = usecase(reviewerRa=repo.reviewers[3].ra, nSelfies=5)
        assert len(reviews) == 5
        assert type(reviewer) == Reviewer
        assert reviewer.__repr__ == repo.reviewers[3].__repr__
        
    def test_get_selfies_to_review_invalid_reviewerRa(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesToReviewUsecase(repo=repo)
        with pytest.raises(EntityError):
            reviews, reviewer = usecase(reviewerRa="210202", nSelfies=2022)

    def test_get_selfies_to_review_reviewerRa_not_found(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesToReviewUsecase(repo=repo)
        with pytest.raises(NoItemsFound):
            reviews, reviewer = usecase(reviewerRa="21022", nSelfies=2022)
    
    def test_get_selfies_to_review_invalid_nSelfies(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesToReviewUsecase(repo=repo)
        with pytest.raises(EntityError):
            reviews, reviewer = usecase(reviewerRa="21022", nSelfies=-2022)
    
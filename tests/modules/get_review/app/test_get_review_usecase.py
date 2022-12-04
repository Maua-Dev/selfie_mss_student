from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.get_review.app.get_review_usecase import GetReviewUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
import pytest

class Test_GetReviewUsecase:
    def test_get_review(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewUsecase(repo=repo)
        
        review = usecase(
            reviewerRa="03026",
            idReview=0
            )
        
        assert review == repo.reviews[0]
    
    def test_get_review_invalid_ra(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewUsecase(repo=repo)
        
        with pytest.raises(EntityError):
            review = usecase(
                reviewerRa=30262,
                idReview=0
            )
            
    def test_get_review_no_items_found(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewUsecase(repo=repo)
        
        with pytest.raises(NoItemsFound):
            review = usecase(
                reviewerRa="30262",
                idReview=0
            )
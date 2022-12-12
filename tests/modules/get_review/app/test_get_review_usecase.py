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
            idReview=repo.reviews[0].idReview,
            idSelfie=repo.reviews[0].selfie.idSelfie,
            studentRa=repo.reviews[0].selfie.student.ra
            )
        
        assert review == repo.reviews[0]
    
    def test_get_review_invalid_studentRa(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewUsecase(repo=repo)
        
        with pytest.raises(EntityError):
            review = usecase(
                idReview=0,
                idSelfie=repo.reviews[0].selfie.idSelfie,
                studentRa=int(repo.reviews[0].selfie.student.ra)
            )
            
    def test_get_review_no_items_found(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewUsecase(repo=repo)
        
        with pytest.raises(NoItemsFound):
            review = usecase(
                idReview=repo.reviews[0].idReview,
                idSelfie=repo.reviews[0].selfie.idSelfie,
                studentRa="21020202"
            )
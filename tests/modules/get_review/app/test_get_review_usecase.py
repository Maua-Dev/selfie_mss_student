from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.get_review.app.get_review_usecase import GetReviewUsecase

class Test_GetReviewUsecase:
    def test_get_review(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewUsecase(repo=repo)
        
        review = usecase(
            reviewerRa="03026",
            idReview=0
            )
        
        assert review == repo.reviews[0]
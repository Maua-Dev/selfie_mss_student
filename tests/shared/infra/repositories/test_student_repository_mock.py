from src.shared.domain.entities.review import Review
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
import datetime
from src.shared.domain.enums.review_state_enum import REVIEW_STATE


class Test_StudentRepositoryMock:
    def test_get_review(self):
        repo = StudentRepositoryMock()
        assert repo.get_review(
            reviewerRa=repo.reviews[0].reviewer.ra,
            idReview=repo.reviews[0].idReview
        ) == repo.reviews[0]
        
    def test_create_review(self):
        repo = StudentRepositoryMock()
        lenBefore = len(repo.reviews)
        
        assert repo.create_review(
            review=Review(
                idReview = 0,
                state=REVIEW_STATE.APPROVED,
                reviewer=repo.reviewers[3],
                selfie=repo.selfies[2],
                dateAssigned=datetime.datetime(2022, 12, 1, 16, 1, 59, 149927),
                dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
              )) == repo.reviews[-1]
        assert lenBefore + 1 == len(repo.reviews)
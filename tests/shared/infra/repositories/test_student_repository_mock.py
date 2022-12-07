from src.shared.domain.entities.review import Review
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
import datetime
from src.shared.domain.enums.review_state_enum import REVIEW_STATE
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE

class Test_StudentRepositoryMock:
    def test_get_review(self):
        repo = StudentRepositoryMock()
        assert repo.get_review(
            reviewerRa=repo.reviews[0].reviewer.ra,
            idReview=repo.reviews[0].idReview,
            idSelfie=repo.reviews[0].selfie.idSelfie,
            studentRa=repo.reviews[0].selfie.student.ra
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
        
    def test_update_review_1(self):
        repo = StudentRepositoryMock()
        review = repo.update_review(
            reviewerRa=repo.reviews[3].reviewer.ra,
            idReview=repo.reviews[3].idReview,
            idSelfie=repo.reviews[3].selfie.idSelfie,
            studentRa=repo.reviews[3].selfie.student.ra,
            new_state=REVIEW_STATE.APPROVED
        )
        
        assert review.__repr__ == repo.reviews[3].__repr__
        assert repo.reviews[3].state == REVIEW_STATE.APPROVED
        assert repo.reviews[3].dateReviewed != datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
        
    def test_update_review_2(self):
        repo = StudentRepositoryMock()
        review = repo.update_review(
            reviewerRa=repo.reviews[3].reviewer.ra,
            idReview=repo.reviews[3].idReview,
            idSelfie=repo.reviews[3].selfie.idSelfie,
            studentRa=repo.reviews[3].selfie.student.ra,
            new_state=REVIEW_STATE.DECLINED,
            new_rejectionDescription="Não gostei da foto.",
            new_rejectionReasons=[REJECTION_REASON.COVERED_FACE, REJECTION_REASON.NOT_ALLOWED_BACKGROUND]
            
        )
        
        assert review.__repr__ == repo.reviews[3].__repr__
        assert repo.reviews[3].state == REVIEW_STATE.DECLINED
        assert repo.reviews[3].selfie.rejectionDescription == "Não gostei da foto."
        assert repo.reviews[3].selfie.rejectionReasons == [REJECTION_REASON.COVERED_FACE, REJECTION_REASON.NOT_ALLOWED_BACKGROUND]
        assert repo.reviews[3].dateReviewed != datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
        
    def test_delete_review(self):
        repo = StudentRepositoryMock()
        lenBefore = len(repo.reviews)
        review = repo.delete_review(
            reviewerRa=repo.reviews[0].reviewer.ra,
            idReview=repo.reviews[0].idReview,
            idSelfie=repo.reviews[0].selfie.idSelfie,
            studentRa=repo.reviews[0].selfie.student.ra
        )
        
        assert review not in repo.reviews
        assert lenBefore == len(repo.reviews) + 1        

    def test_get_pending_validation_selfies_assigned_four_selfies(self):
        repo = StudentRepositoryMock()
        selfies = repo.get_pending_validation_selfies_assigned(repo.reviewers[3].ra)
        assert len(selfies) == 4
        
    def test_get_pending_validation_selfies_assigned_no_selfies(self):
        repo = StudentRepositoryMock()
        selfies = repo.get_pending_validation_selfies_assigned(reviewerRa=repo.reviewers[0].ra)
        assert len(selfies) == 0
        
    def test_assign_selfies(self):
        repo = StudentRepositoryMock()
        
        lenBeforeSelfiesAssigned = len(repo.get_pending_validation_selfies_assigned(reviewerRa=repo.reviewers[0].ra))
        lenBeforeSelfiesPendingReview = len([selfie for selfie in repo.selfies if selfie.state == STATE.PENDING_REVIEW])
        selfies = repo.assign_selfies(reviewerRa=repo.reviewers[0].ra, nSelfies=1)
        
        new_selfies = [selfie for selfie in repo.selfies if selfie.state == STATE.PENDING_REVIEW]
        assert len(selfies) == lenBeforeSelfiesAssigned + 1
        assert lenBeforeSelfiesPendingReview == len(new_selfies) + 1
        for selfie in selfies:
            assert selfie not in new_selfies
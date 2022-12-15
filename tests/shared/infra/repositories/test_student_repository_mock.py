from src.shared.domain.entities.review import Review
from src.shared.domain.entities.reviewer import Reviewer
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
import datetime
from src.shared.domain.enums.review_state_enum import REVIEW_STATE
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.entities.automatic_review import AutomaticReview
from src.shared.domain.entities.label import Label
from src.shared.domain.entities.selfie import Selfie



class Test_StudentRepositoryMock:
    def test_get_review(self):
        repo = StudentRepositoryMock()
        assert repo.get_review(
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

    def test_get_pending_validation_selfies_assigned_one(self):
        repo = StudentRepositoryMock()
        reviews = repo.get_pending_validation_selfies_assigned(reviewerRa=repo.reviewers[3].ra)
        assert len(reviews) == 2
        assert type(reviews[0]) == Review
        
    def test_get_pending_validation_selfies_assigned_no_selfies(self):
        repo = StudentRepositoryMock()
        reviews = repo.get_pending_validation_selfies_assigned(reviewerRa=repo.reviewers[0].ra)
        assert len(reviews) == 0
        
    def test_assign_selfies(self):
        repo = StudentRepositoryMock()
        
        lenBeforeSelfiesAssigned = len(repo.get_pending_validation_selfies_assigned(reviewerRa=repo.reviewers[0].ra))
        lenBeforeSelfiesPendingReview = len([selfie for selfie in repo.selfies if selfie.state == STATE.PENDING_REVIEW])
        reviews = repo.assign_selfies(reviewer=repo.reviewers[0], nSelfies=1)
        
        new_selfies = [selfie for selfie in repo.selfies if selfie.state == STATE.PENDING_REVIEW]
        assert len(reviews) == lenBeforeSelfiesAssigned + 1
        assert lenBeforeSelfiesPendingReview == len(new_selfies) + 1
        for review in reviews:
            assert review.selfie not in new_selfies
            
    def test_selfies_to_review_adding_one_selfie(self):
        repo = StudentRepositoryMock()
        len_before_assignment = len(repo.get_pending_validation_selfies_assigned(reviewerRa=repo.reviewers[3].ra))
        
        selfies_to_review, reviewer = repo.get_selfies_to_review(reviewerRa=repo.reviewers[3].ra, nSelfies=5)
        
        assert len(selfies_to_review) == len_before_assignment + 1
        assert type(reviewer) == Reviewer
            
    def test_selfies_to_review_adding_one_selfie_but_cannot_complete_seven_selfies(self):
        repo = StudentRepositoryMock()
        len_before_assignment = len(repo.get_pending_validation_selfies_assigned(reviewerRa=repo.reviewers[3].ra))
        
        selfies_to_review, reviewer = repo.get_selfies_to_review(reviewerRa=repo.reviewers[3].ra, nSelfies=7)
        
        assert len(selfies_to_review) == len_before_assignment + 1
        assert reviewer.ra == repo.reviewers[3].ra
        
    def test_selfies_to_review_complete_seven_selfies(self):
        repo = StudentRepositoryMock()
        len_before_assignment = len(repo.get_pending_validation_selfies_assigned(reviewerRa=repo.reviewers[3].ra))
        len_selfies_created_pending_review = 4
        for i in range(len_selfies_created_pending_review):
            repo.create_selfie(Selfie(
                idSelfie=0,
                student=repo.students[6],
                dateCreated=datetime.datetime(2022, 10, 1, 16, 1, 59, 149927),
                url=f"https://i.imgur.com/0K{i}BHTB.jpg",
                state=STATE.PENDING_REVIEW,
                rejectionReasons=[],
                rejectionDescription="",
                automaticReview=AutomaticReview(
                    automaticallyRejected=False,
                    rejectionReasons=[],
                    labels=[
                        Label(
                            name="Person",
                            coords={
                                "Width": 0.9711952805519104,
                                "Height": 0.8659809827804565,
                                "Left": 0.012313545681536198,
                                "Top": 0.11108686774969101
                            },
                            confidence=98.54370880126953,
                            parents=[],
                        ),
                        Label(
                            name="Face",
                            coords={
                                "Width": 0.9711952805519104,
                                "Height": 0.8659809827804565,
                                "Left": 0.012313545681536198,
                                "Top": 0.11108686774969101
                            },
                            confidence=98.54370880126953,
                            parents=[],
                        ),
                    ]
                )
            ))
        
        selfies_to_review, reviewer = repo.get_selfies_to_review(reviewerRa=repo.reviewers[3].ra, nSelfies=7)
        len_selfies_pending_review_in_mock = 1
        assert len(selfies_to_review) == len_before_assignment + len_selfies_created_pending_review + len_selfies_pending_review_in_mock
        
    def test_selfies_to_review_already_have_two_selfies(self):
        repo = StudentRepositoryMock()
        len_before_assignment = len(repo.get_pending_validation_selfies_assigned(reviewerRa=repo.reviewers[3].ra))
        
        selfies_to_review, reviewer = repo.get_selfies_to_review(reviewerRa=repo.reviewers[3].ra, nSelfies=2)
        
        assert len(selfies_to_review) == len_before_assignment 
        assert type(selfies_to_review[0]) == Review

    def test_approve_selfie(self):
        repo = StudentRepositoryMock()
        review = repo.approve_selfie(
            idReview=repo.reviews[3].idReview,
            idSelfie=repo.reviews[3].selfie.idSelfie,
            studentRa=repo.reviews[3].selfie.student.ra
        )
        
        assert review.__repr__ == repo.reviews[3].__repr__
        assert review.state == REVIEW_STATE.APPROVED
        assert review.selfie.state == STATE.APPROVED
        
    def test_reject_selfie(self):
        repo = StudentRepositoryMock()
        review = repo.reject_selfie(
            idReview=repo.reviews[3].idReview,
            idSelfie=repo.reviews[3].selfie.idSelfie,
            studentRa=repo.reviews[3].selfie.student.ra,
            new_rejectionDescription="Está com fone de ouvido",
            new_rejectionReasons=[REJECTION_REASON.COVERED_FACE]
        )
        
        assert review.__repr__ == repo.reviews[3].__repr__
        assert review.state == REVIEW_STATE.DECLINED
        assert review.selfie.rejectionReasons == [REJECTION_REASON.COVERED_FACE]
        assert review.selfie.rejectionDescription == "Está com fone de ouvido"
        assert review.selfie.state == STATE.DECLINED
        


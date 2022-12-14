from src.shared.domain.enums.review_state_enum import REVIEW_STATE
from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.approve_selfie.app.approve_selfie_usecase import ApproveSelfieUsecase
import pytest

class Test_ApproveSelfie:
    def test_approve_selfie(self):
        repo = StudentRepositoryMock()
        usecase = ApproveSelfieUsecase(repo=repo)
        
        assert repo.selfies[10].state == STATE.IN_REVIEW
        review = usecase(
            idReview=repo.reviews[3].idReview,
            idSelfie=repo.reviews[3].selfie.idSelfie,
            studentRa=repo.reviews[3].selfie.student.ra
            )
        
        assert review == repo.reviews[3]
        assert review.state == REVIEW_STATE.APPROVED
        assert review.selfie.state == STATE.APPROVED
        assert repo.selfies[10].state == STATE.APPROVED
        
    def test_approve_selfie_forbidden_action(self):
        
        repo = StudentRepositoryMock()
        usecase = ApproveSelfieUsecase(repo=repo)
        
        with pytest.raises(ForbiddenAction):
            review = usecase(
                idReview=repo.reviews[0].idReview,
                idSelfie=repo.reviews[0].selfie.idSelfie,
                studentRa=repo.reviews[0].selfie.student.ra
                )
            
    def test_approve_invalid_studentRa(self):
        repo = StudentRepositoryMock()
        usecase = ApproveSelfieUsecase(repo=repo)
        
        with pytest.raises(EntityError):
            review = usecase(
                idReview=0,
                idSelfie=repo.reviews[0].selfie.idSelfie,
                studentRa=int(repo.reviews[0].selfie.student.ra)
            )
            
    def test_approve_no_items_found(self):
        repo = StudentRepositoryMock()
        usecase = ApproveSelfieUsecase(repo=repo)
        
        with pytest.raises(NoItemsFound):
            review = usecase(
                idReview=repo.reviews[0].idReview,
                idSelfie=repo.reviews[0].selfie.idSelfie,
                studentRa="12345678"
            )            
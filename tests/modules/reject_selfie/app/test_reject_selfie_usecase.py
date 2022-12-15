from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.reject_selfie.app.reject_selfie_usecase import RejectSelfieUsecase
import pytest

class Test_RejectSelfieUsecase:
    def test_reject_selfie(self):
        repo = StudentRepositoryMock()
        usecase = RejectSelfieUsecase(repo=repo)
        
        review = usecase(
            idReview=repo.reviews[3].idReview,
            idSelfie=repo.reviews[3].selfie.idSelfie,
            studentRa=repo.reviews[3].selfie.student.ra,
            new_rejectionDescription="Está com fone de ouvido",
            new_rejectionReasons=[REJECTION_REASON.COVERED_FACE]
            )
        
        assert review == repo.reviews[3]
        
    def test_reject_selfie_forbidden_action(self):
        
        repo = StudentRepositoryMock()
        usecase = RejectSelfieUsecase(repo=repo)
        
        with pytest.raises(ForbiddenAction):
            review = usecase(
                idReview=repo.reviews[0].idReview,
                idSelfie=repo.reviews[0].selfie.idSelfie,
                studentRa=repo.reviews[0].selfie.student.ra
                )
            
    def test_reject_invalid_studentRa(self):
        repo = StudentRepositoryMock()
        usecase = RejectSelfieUsecase(repo=repo)
        
        with pytest.raises(EntityError):
            review = usecase(
                idReview=0,
                idSelfie=repo.reviews[0].selfie.idSelfie,
                studentRa=int(repo.reviews[0].selfie.student.ra)
            )
            
    def test_reject_no_items_found(self):
        repo = StudentRepositoryMock()
        usecase = RejectSelfieUsecase(repo=repo)
        
        with pytest.raises(NoItemsFound):
            review = usecase(
                idReview=repo.reviews[0].idReview,
                idSelfie=repo.reviews[0].selfie.idSelfie,
                studentRa="21009317"
            )       
                 
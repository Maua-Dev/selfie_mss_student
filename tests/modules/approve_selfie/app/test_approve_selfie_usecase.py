from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.approve_selfie.app.approve_selfie_usecase import ApproveSelfieUsecase
import pytest

class Test_ApproveSelfie:
    def test_approve_selfie(self):
        repo = StudentRepositoryMock()
        usecase = ApproveSelfieUsecase(repo=repo)
        
        review = usecase(
            reviewerRa=repo.reviews[3].reviewer.ra,
            idReview=repo.reviews[3].idReview,
            idSelfie=repo.reviews[3].selfie.idSelfie,
            studentRa=repo.reviews[3].selfie.student.ra
            )
        
        assert review == repo.reviews[3]
        
    def test_approve_selfie_forbidden_action(self):
        
        repo = StudentRepositoryMock()
        usecase = ApproveSelfieUsecase(repo=repo)
        
        with pytest.raises(ForbiddenAction):
            review = usecase(
                reviewerRa=repo.reviews[0].reviewer.ra,
                idReview=repo.reviews[0].idReview,
                idSelfie=repo.reviews[0].selfie.idSelfie,
                studentRa=repo.reviews[0].selfie.student.ra
                )
            
    def test_approve_invalid_reviewerRa(self):
        repo = StudentRepositoryMock()
        usecase = ApproveSelfieUsecase(repo=repo)
        
        with pytest.raises(EntityError):
            review = usecase(
                reviewerRa=30262,
                idReview=0,
                idSelfie=repo.reviews[0].selfie.idSelfie,
                studentRa=repo.reviews[0].selfie.student.ra
            )
            
    def test_approve_invalid_studentRa(self):
        repo = StudentRepositoryMock()
        usecase = ApproveSelfieUsecase(repo=repo)
        
        with pytest.raises(EntityError):
            review = usecase(
                reviewerRa="30262",
                idReview=0,
                idSelfie=repo.reviews[0].selfie.idSelfie,
                studentRa=int(repo.reviews[0].selfie.student.ra)
            )
            
    def test_approve_no_items_found(self):
        repo = StudentRepositoryMock()
        usecase = ApproveSelfieUsecase(repo=repo)
        
        with pytest.raises(NoItemsFound):
            review = usecase(
                reviewerRa="30262",
                idReview=repo.reviews[0].idReview,
                idSelfie=repo.reviews[0].selfie.idSelfie,
                studentRa=repo.reviews[0].selfie.student.ra
            )            
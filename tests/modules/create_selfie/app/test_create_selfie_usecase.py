from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.modules.create_selfie.app.create_selfie_usecase import CreateSelfieUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.helpers.functions.read_automatic_review import read_automatic_review
from src.shared.domain.enums.state_enum import STATE
import pytest


AUTOMATIC_REVIEW_DICT = {
            "automaticallyRejected": "False",
            "rejectionReasons": ["NONE"],
            "labels": [{
                            "name": "Glasses",
                            "coords": {
                                    "Width": "0.6591288447380066",
                                    "Height": "0.17444363236427307",
                                    "Left": "0.19148917496204376",
                                    "Top": "0.3813813030719757"
                            },
                            "confidence": "94.5357666015625",
                            "parents": ["Accessories"],
                        },
                        {
                            "name": "Blalblas",
                            "coords": {
                                    "Width": "0.6591288480066",
                                    "Height": "0.1744236427307",
                                    "Left": "0.19148916204376",
                                    "Top": "0.3813813719757"
                            },
                            "confidence": "95.5366015625",
                            "parents": ["ASODnoasdsa", "nmdokasnkndkasnkd"],
                        }]
                  }

class Test_CreateSelfieUsecase:
    def test_create_selfie_usecase(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)

        lenBefore = len(repo.selfies)

        selfie = usecase(ra="21014442", url="https://www.youtube.com/watch?v=k85mRPqvMbE", automaticReview=AUTOMATIC_REVIEW_DICT)

        lenAfter = lenBefore + 1

        assert len(repo.selfies) == lenAfter
        assert repo.selfies[lenAfter - 1].url == "https://www.youtube.com/watch?v=k85mRPqvMbE"
        assert repo.selfies[lenAfter - 1].rejectionReasons == [REJECTION_REASON.NONE]
        assert repo.selfies[lenAfter - 1].student.ra == "21014442"
        assert repo.selfies[lenAfter - 1].student.name == repo.students[1].name
        assert repo.selfies[lenAfter - 1].student.email == repo.students[1].email
        assert repo.selfies[lenAfter - 1].automaticReview.automaticallyRejected == read_automatic_review(automaticReview=AUTOMATIC_REVIEW_DICT).automaticallyRejected
        assert selfie.idSelfie == 1

    def test_create_selfie_usecase_automaticallyRejected(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)

        lenBefore = len(repo.selfies)

        automaticReviewDict = {
            "automaticallyRejected": "True",
            "rejectionReasons": ["COVERED_FACE", "NO_PERSON_RECOGNIZED"],
            "labels": [{
                            "name": "Glasses",
                            "coords": {
                                    "Width": "0.6591288447380066",
                                    "Height": "0.17444363236427307",
                                    "Left": "0.19148917496204376",
                                    "Top": "0.3813813030719757"
                            },
                            "confidence": "94.5357666015625",
                            "parents": ["Accessories"],
                        },
                        {
                            "name": "Blalblas",
                            "coords": {
                                    "Width": "0.6591288480066",
                                    "Height": "0.1744236427307",
                                    "Left": "0.19148916204376",
                                    "Top": "0.3813813719757"
                            },
                            "confidence": "95.5366015625",
                            "parents": ["ASODnoasdsa", "nmdokasnkndkasnkd"],
                        }]
                  }
    
        lenAfter = lenBefore + 1
        selfie = usecase(ra="21014442", url="https://www.youtube.com/watch?v=k85mRPqvMbE", automaticReview=automaticReviewDict)


        assert len(repo.selfies) == lenAfter
        assert repo.selfies[lenAfter - 1].url == "https://www.youtube.com/watch?v=k85mRPqvMbE"
        assert repo.selfies[lenAfter - 1].state == STATE.DECLINED
        assert repo.selfies[lenAfter - 1].rejectionReasons == [REJECTION_REASON.COVERED_FACE, REJECTION_REASON.NO_PERSON_RECOGNIZED]
        
        assert repo.selfies[lenAfter - 1].student.ra == "21014442"
        assert repo.selfies[lenAfter - 1].student.name == repo.students[1].name
        assert repo.selfies[lenAfter - 1].student.email == repo.students[1].email
        assert repo.selfies[lenAfter - 1].automaticReview.automaticallyRejected == read_automatic_review(automaticReview=automaticReviewDict).automaticallyRejected
        assert selfie.idSelfie == 1


    def test_create_selfie_usecase_ra_not_found(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)

        with pytest.raises(NoItemsFound):
            usecase(ra="12345678", url="https://www.youtube.com/watch?v=k85mRPqvMbE", automaticReview=AUTOMATIC_REVIEW_DICT)
            
    def test_create_selfie_usecase_invalid_ra(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)

        with pytest.raises(EntityError):
            usecase(ra="123456782", url="https://www.youtube.com/watch?v=k85mRPqvMbE", automaticReview=AUTOMATIC_REVIEW_DICT)
            
    def test_create_selfie_usecase_invalid_url(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)

        with pytest.raises(EntityError):
            usecase(ra="21014442", url="www.mamaco.com", automaticReview=AUTOMATIC_REVIEW_DICT)
            
    def test_create_selfie_usecase_student_have_approved_selfie(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)

        with pytest.raises(ForbiddenAction):
            usecase(ra="15013103", url="www.mamaco.com", automaticReview=AUTOMATIC_REVIEW_DICT)
    
    def test_create_selfie_usecase_error_automatic_review_missing_parameter(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)
        
        automatic_review = {
            "automaticallyRejected": "True",
            "rejectionReasons": "COVERED_FACE",
            "labels": [{
                            "name": "Glasses",
                            "coords": {
                                    "Width": "0.6591288447380066",
                                    "Height": "0.17444363236427307",
                                    "Left": "0.19148917496204376",
                                    "Top": "0.3813813030719757"
                            },
                            "confidence": "94.5357666015625",
                            "parents": ["Accessories"],
                        },
                        { # missing name
                            "coords": {
                                    "Width": "0.6591288480066",
                                    "Height": "0.1744236427307",
                                    "Left": "0.19148916204376",
                                    "Top": "0.3813813719757"
                            },
                            "confidence": "95.5366015625",
                            "parents": ["ASODnoasdsa", "nmdokasnkndkasnkd"],
                        }]
                  }

        with pytest.raises(MissingParameters):
            usecase(ra="21014442", url="www.mamaco.com", automaticReview=automatic_review)


     
    def test_create_selfie_usecase_error_automatic_review_wrong_type(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)

        with pytest.raises(EntityError):
            usecase(ra="21014442", url="www.mamaco.com", automaticReview=1)
        
    
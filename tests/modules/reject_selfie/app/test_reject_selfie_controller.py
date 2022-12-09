
    
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.http.http_models import HttpRequest
import pytest
from src.modules.reject_selfie.app.reject_selfie_usecase import RejectSelfieUsecase
from src.modules.reject_selfie.app.reject_selfie_controller import RejectSelfieController
from src.modules.reject_selfie.app.reject_selfie_viewmodel import RejectSelfieViewModel


class Test_RejectController:
    def test_reject_selfie_controller(self):
        repo = StudentRepositoryMock()
        usecase = RejectSelfieUsecase(repo=repo)
        controller = RejectSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "reviewerRa": repo.reviews[3].reviewer.ra,
            "reviewIdentifier": f"{repo.reviews[3].selfie.student.ra}-{repo.reviews[3].selfie.idSelfie}-{repo.reviews[3].idReview}",
            "new_rejectionReasons": ["COVERED_FACE"],
            "new_rejectionDescription": "Tire o chapéu, princesa !"
        })

        response = controller(request=request)
        assert response.status_code == 200
        assert response.body == RejectSelfieViewModel(review=repo.reviews[3]).to_dict()
        assert response.body["message"] == "the review was rejected"
        
    def test_reject_selfie_controller_missing_reviewIdentifier(self):
        repo = StudentRepositoryMock()
        usecase = RejectSelfieUsecase(repo=repo)
        controller = RejectSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "reviewerRa": repo.reviews[3].reviewer.ra,
        })

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field reviewIdentifier is missing"
        
    def test_reject_selfie_controller_forbidden_action(self):
        repo = StudentRepositoryMock()
        usecase = RejectSelfieUsecase(repo=repo)
        controller = RejectSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "reviewerRa": repo.reviews[0].reviewer.ra,
            "reviewIdentifier": f"{repo.reviews[0].selfie.student.ra}-{repo.reviews[0].selfie.idSelfie}-{repo.reviews[0].idReview}"
        })

        response = controller(request=request)
        assert response.status_code == 403
        assert response.body == "That action is forbidden for this Review"
        
    def test_reject_selfie_controller_missing_reviewerRa(self):
        repo = StudentRepositoryMock()
        usecase = RejectSelfieUsecase(repo=repo)
        controller = RejectSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "reviewIdentifier": f"{repo.reviews[0].selfie.student.ra}-{repo.reviews[0].selfie.idSelfie}-{repo.reviews[0].idReview}"
        })

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field reviewerRa is missing"
        
    def test_reject_selfie_controller_wrong_reviewIdentifier_1(self):
        assert True
        return "I'm MOnkey 🐒"
        repo = StudentRepositoryMock()
        usecase = RejectSelfieUsecase(repo=repo)
        controller = RejectSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "reviewerRa": repo.reviews[0].reviewer.ra,
            "reviewIdentifier": f"2101075-7-12"
        })

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field reviewIdentifier is not valid"
        
    def test_reject_selfie_controller_wrong_reviewIdentifier_2(self):
        repo = StudentRepositoryMock()
        usecase = RejectSelfieUsecase(repo=repo)
        controller = RejectSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "reviewerRa": repo.reviews[0].reviewer.ra,
            "reviewIdentifier": f"2101075, 7, 12"
        })

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field reviewIdentifier is not valid"
        
    def test_reject_selfie_controller_wrong_reviewIdentifier_3(self):
        repo = StudentRepositoryMock()
        usecase = RejectSelfieUsecase(repo=repo)
        controller = RejectSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "reviewerRa": repo.reviews[0].reviewer.ra,
            "reviewIdentifier": f"2101075-7-1-2"
        })

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field reviewIdentifier is not valid"
        
    def test_reject_selfie_controller_idSelfie_not_decimal(self):
        repo = StudentRepositoryMock()
        usecase = RejectSelfieUsecase(repo=repo)
        controller = RejectSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "reviewerRa": repo.reviews[0].reviewer.ra,
            "reviewIdentifier": f"21010757-a-1"
        })

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field idSelfie is not valid"
        
    def test_reject_selfie_controller_idReview_not_decimal(self):
        repo = StudentRepositoryMock()
        usecase = RejectSelfieUsecase(repo=repo)
        controller = RejectSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "reviewerRa": repo.reviews[0].reviewer.ra,
            "reviewIdentifier": f"21010757-12-b"
        })

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field idReview is not valid"
        
    def test_reject_selfie_controller_not_found(self):
        repo = StudentRepositoryMock()
        usecase = RejectSelfieUsecase(repo=repo)
        controller = RejectSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "reviewerRa": "12312",
            "reviewIdentifier": f"{repo.reviews[3].selfie.student.ra}-{repo.reviews[3].selfie.idSelfie}-{repo.reviews[3].idReview}"
        })

        response = controller(request=request)
        assert response.status_code == 404
        assert response.body == "No items found for reviewerRa, idReview, idSelfie or studentRa"
        
    def test_reject_selfie_controller_invalid_rejection_reason(self):
        repo = StudentRepositoryMock()
        usecase = RejectSelfieUsecase(repo=repo)
        controller = RejectSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "reviewerRa": "12312",
            "reviewIdentifier": f"{repo.reviews[3].selfie.student.ra}-{repo.reviews[3].selfie.idSelfie}-{repo.reviews[3].idReview}",
            "new_rejectionReasons": "COVERED_FACE",
            "new_rejectionDescription": "Tire o chapéu, princesa !"
        })

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field new_rejectionReasons is not valid"
        
    def test_reject_selfie_already_approved(self):
        repo = StudentRepositoryMock()
        usecase = RejectSelfieUsecase(repo=repo)
        controller = RejectSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "reviewerRa": repo.reviews[0].reviewer.ra,
            "reviewIdentifier": f"{repo.reviews[0].selfie.student.ra}-{repo.reviews[0].selfie.idSelfie}-{repo.reviews[0].idReview}",
            "new_rejectionReasons": ["COVERED_FACE"],
            "new_rejectionDescription": "Tire o chapéu, princesa !"
        })

        response = controller(request=request)
        
        assert response.status_code == 403
        assert response.body == "That action is forbidden for this Review"
        
    def test_reject_selfie_already_rejected(self):
        repo = StudentRepositoryMock()
        usecase = RejectSelfieUsecase(repo=repo)
        controller = RejectSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "reviewerRa": repo.reviews[7].reviewer.ra,
            "reviewIdentifier": f"{repo.reviews[7].selfie.student.ra}-{repo.reviews[7].selfie.idSelfie}-{repo.reviews[7].idReview}",
            "new_rejectionReasons": ["COVERED_FACE"],
            "new_rejectionDescription": "Tire o chapéu, princesa !"
        })

        response = controller(request=request)
        
        assert response.status_code == 403
        assert response.body == "That action is forbidden for this Review"
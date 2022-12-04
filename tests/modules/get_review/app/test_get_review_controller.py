from src.modules.get_review.app.get_review_usecase import GetReviewUsecase
from src.modules.get_review.app.get_review_controller import GetReviewController
from src.modules.get_review.app.get_review_viewmodel import GetReviewViewModel 
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.http.http_models import HttpRequest



class Test_GetReviewController:
    def test_get_review_controller(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewUsecase(repo=repo)
        controller = GetReviewController(usecase=usecase)

        request = HttpRequest(query_params={
            "reviewerRa": repo.reviews[0].reviewer.ra,
            "idReview": str(repo.reviews[0].idReview)
        })

        response = controller(request=request)
        assert response.status_code == 200
        assert response.body == GetReviewViewModel(review=repo.reviews[0]).to_dict()
        
    def test_get_review_controller_missing_reviewerRa(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewUsecase(repo=repo)
        controller = GetReviewController(usecase=usecase)

        request = HttpRequest(query_params={
            "idReview": str(repo.reviews[0].idReview)
        })

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field reviewerRa is missing"
        
    def test_get_review_controller_missing_idReview(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewUsecase(repo=repo)
        controller = GetReviewController(usecase=usecase)

        request = HttpRequest(query_params={
            "reviewerRa": repo.reviews[0].reviewer.ra
        })

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field idReview is missing"
        
        
    def test_get_review_controller_wrong_idReview_type(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewUsecase(repo=repo)
        controller = GetReviewController(usecase=usecase)

        request = HttpRequest(query_params={
            "reviewerRa": repo.reviews[0].reviewer.ra,
            "idReview": repo.reviews[0].idReview
        })

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field idReview isn\'t in the right type.\n Received: int.\n Expected: str"
        
    def test_get_review_controller_idReview_not_decimal(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewUsecase(repo=repo)
        controller = GetReviewController(usecase=usecase)

        request = HttpRequest(query_params={
            "reviewerRa": repo.reviews[0].reviewer.ra,
            "idReview": "repo.reviews[0].idReview"
        })

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field idReview is not valid"
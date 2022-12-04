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
            "fullIdReview": f"{repo.reviews[0].selfie.student.ra}-{repo.reviews[0].selfie.idSelfie}-{repo.reviews[0].idReview}"
        })

        response = controller(request=request)
        assert response.status_code == 200
        assert response.body == GetReviewViewModel(review=repo.reviews[0]).to_dict()
        
    def test_get_review_controller_missing_fullIdReview(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewUsecase(repo=repo)
        controller = GetReviewController(usecase=usecase)

        request = HttpRequest(query_params={
            "reviewerRa": repo.reviews[0].reviewer.ra,
        })

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field fullIdReview is missing"
        
    def test_get_review_controller_missing_reviewerRa(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewUsecase(repo=repo)
        controller = GetReviewController(usecase=usecase)

        request = HttpRequest(query_params={
            "fullIdReview": f"{repo.reviews[0].selfie.student.ra}-{repo.reviews[0].selfie.idSelfie}-{repo.reviews[0].idReview}"
        })

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field reviewerRa is missing"
        
        
    def test_get_review_controller_wrong_fullIdReview_1(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewUsecase(repo=repo)
        controller = GetReviewController(usecase=usecase)

        request = HttpRequest(query_params={
            "reviewerRa": repo.reviews[0].reviewer.ra,
            "fullIdReview": f"2101075-7-12"
        })

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field fullIdReview is not valid"
        
    def test_get_review_controller_wrong_fullIdReview_2(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewUsecase(repo=repo)
        controller = GetReviewController(usecase=usecase)

        request = HttpRequest(query_params={
            "reviewerRa": repo.reviews[0].reviewer.ra,
            "fullIdReview": f"2101075, 7, 12"
        })

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field fullIdReview is not valid"
        
    def test_get_review_controller_wrong_fullIdReview_3(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewUsecase(repo=repo)
        controller = GetReviewController(usecase=usecase)

        request = HttpRequest(query_params={
            "reviewerRa": repo.reviews[0].reviewer.ra,
            "fullIdReview": f"2101075-7-1-2"
        })

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field fullIdReview is not valid"
        
    def test_get_review_controller_idSelfie_not_decimal(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewUsecase(repo=repo)
        controller = GetReviewController(usecase=usecase)

        request = HttpRequest(query_params={
            "reviewerRa": repo.reviews[0].reviewer.ra,
            "fullIdReview": f"21010757-a-1"
        })

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field idSelfie is not valid"
        
    def test_get_review_controller_idReview_not_decimal(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewUsecase(repo=repo)
        controller = GetReviewController(usecase=usecase)

        request = HttpRequest(query_params={
            "reviewerRa": repo.reviews[0].reviewer.ra,
            "fullIdReview": f"21010757-12-b"
        })

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field idReview is not valid"
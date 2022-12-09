from src.modules.get_selfies_to_review.app.get_selfies_to_review_controller import GetSelfiesToReviewController
from src.modules.get_selfies_to_review.app.get_selfies_to_review_usecase import GetSelfiesToReviewUsecase
from src.shared.helpers.http.http_models import HttpRequest
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock


class Test_GetSelfiesToReviewController:
    def test_get_selfies_to_review_controller(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesToReviewUsecase(repo=repo)
        controller = GetSelfiesToReviewController(usecase=usecase)

        request = HttpRequest(query_params={
            "reviewerRa": repo.reviews[3].reviewer.ra,
            "nSelfies": "5"
        })

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body["message"] == "the reviews were retriven"
        assert len(response.body["reviews"]) == 5

    def test_get_selfies_to_review_controller_none_nSelfies(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesToReviewUsecase(repo=repo)
        controller = GetSelfiesToReviewController(usecase=usecase)

        request = HttpRequest(query_params={
            "reviewerRa": repo.reviews[3].reviewer.ra,
        })

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body["message"] == "the reviews were retriven"

    def test_get_selfies_to_review_controller_reviewerRa_not_found(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesToReviewUsecase(repo=repo)
        controller = GetSelfiesToReviewController(usecase=usecase)

        request = HttpRequest(query_params={
            "reviewerRa": "12345",
            "nSelfies": "5"
        })

        response = controller(request=request)

        assert response.status_code == 404
        assert response.body == "No items found for reviewerRa"

    def test_get_selfies_to_review_controller_nSelfies_not_decimal(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesToReviewUsecase(repo=repo)
        controller = GetSelfiesToReviewController(usecase=usecase)

        request = HttpRequest(query_params={
            "reviewerRa": "2020202202020200202020020202",
            "nSelfies": "eu sou o brancas (emoji de oculos escuro)"
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field nSelfies is not valid"
    
    def test_get_selfies_to_review_controller_invalid_reviewerRa(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesToReviewUsecase(repo=repo)
        controller = GetSelfiesToReviewController(usecase=usecase)

        request = HttpRequest(query_params={
            "reviewerRa": "2020202202020200202020020202",
            "nSelfies": "5"
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field reviewerRa is not valid"

    def test_get_selfies_to_review_controller_nSelfies_must_be_string(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesToReviewUsecase(repo=repo)
        controller = GetSelfiesToReviewController(usecase=usecase)

        request = HttpRequest(query_params={
            "reviewerRa": "2020202202020200202020020202",
            "nSelfies": 5
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field nSelfies is not valid"

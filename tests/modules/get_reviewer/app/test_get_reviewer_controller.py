
from src.modules.get_reviewer.app.get_reviewer_controller import GetReviewerController
from src.modules.get_reviewer.app.get_reviewer_usecase import GetReviewerUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.http.http_models import HttpRequest



class Test_GetReviewerController:
    def test_get_reviewer_controller(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewerUsecase(repo=repo)
        controller = GetReviewerController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "03026",
        })

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body['name'] == "Mauro Crapino"
        assert response.body['ra'] == "03026"
        assert response.body['email'] == "mauro@maua.br"

    def test_get_reviewer_controller_no_items_found(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewerUsecase(repo=repo)
        controller = GetReviewerController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "03027",
        })

        response = controller(request=request)

        assert response.body == "No items found for Reviewer"
        assert response.status_code == 404

    def test_get_reviewer_controller_bad_request(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewerUsecase(repo=repo)
        controller = GetReviewerController(usecase=usecase)

        request = HttpRequest(query_params={
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field ra is missing"

    def test_get_reviewer_controller_bad_request_int(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewerUsecase(repo=repo)
        controller = GetReviewerController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": 30271,
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "ra must be a string"

    def test_get_reviewer_controller_bad_request_invalid_ra(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewerUsecase(repo=repo)
        controller = GetReviewerController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "3027",
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field ra is not valid"

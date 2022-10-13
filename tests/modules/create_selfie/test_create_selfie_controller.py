from src.domain.entities.student import Student
from src.modules.create_selfie.create_selfie_usecase import CreateSelfieUsecase
from src.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.create_selfie.create_selfie_controller import CreateSelfieController
from src.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound


class Test_CreateSelfieController:

    def test_create_selfie_controller(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)
        controller = CreateSelfieController(usecase=usecase)
        request = HttpRequest(query_params={
            "ra": "21010757",
            "url": "https://www.youtube.com/watch?v=5IpYOF4Hi6Q",
        })
        
        lenBefore = len(repo.selfies)
        response = controller(request=request)

        lenAfter = lenBefore + 1

        assert len(repo.selfies) == lenAfter
        assert response.body["url"] == "https://www.youtube.com/watch?v=5IpYOF4Hi6Q"
        assert response.body["idSelfie"] == 2
        assert response.body["student"]["ra"] == "21010757"
        assert response.status_code == 201
        assert response.body["message"] == "the selfie was created"

    def test_create_selfie_controller_missing_ra(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)
        controller = CreateSelfieController(usecase=usecase)
        request = HttpRequest(query_params={
            "url": "https://www.youtube.com/watch?v=5IpYOF4Hi6Q",
        })
        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field ra is missing"

    def test_create_selfie_controller_missing_url(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)
        controller = CreateSelfieController(usecase=usecase)
        request = HttpRequest(query_params={
            "ra": "21002008",
        })
        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field url is missing"

   
    def test_create_selfie_controller_bad_request_int(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)
        controller = CreateSelfieController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": 21002088,
            "url": "https://www.youtube.com/watch?v=5IpYOF4Hi6Q"
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "ra must be a string"

    def test_create_selfie_controller_bad_request_invalid_ra_dash(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)
        controller = CreateSelfieController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "2100208-8",
            "url": "https://www.youtube.com/watch?v=5IpYOF4Hi6Q"
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field ra is not valid"

    def test_create_selfie_controller_no_ra_found(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)
        controller = CreateSelfieController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "12345678",
            "url": "https://www.youtube.com/watch?v=5IpYOF4Hi6Q"
        })

        response = controller(request=request)

        assert response.status_code == 404
        assert response.body == "No items found for ra"
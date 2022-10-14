from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound
from src.modules.get_selfies_by_ra.get_selfies_by_ra_usecase import GetSelfiesByRaUsecase
from src.modules.get_selfies_by_ra.get_selfies_by_ra_controller import GetSelfiesByRaController



class Test_GetSelfiesByRaController:
    def test_get_selfies_by_ra_controller(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesByRaUsecase(repo=repo)
        controller = GetSelfiesByRaController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": repo.students[0].ra,
        })

        response = controller(request=request)

        assert response.status_code == 200
        assert len(response.body['selfies']) == 2
        assert response.body['student']['name'] == repo.students[0].name
        assert response.body['selfies'][0]['rejectionReason'] == "COVERED_FACE"
        assert response.body['selfies'][0]['rejectionDescription'] == "Balaclava"
        assert response.body['message'] == "the selfies were retriven"
        
    def test_get_selfies_by_ra_controller_no_selfies(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesByRaUsecase(repo=repo)
        controller = GetSelfiesByRaController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": repo.students[4].ra,
        })

        response = controller(request=request)

        assert response.status_code == 200
        assert len(response.body['selfies']) == 0
        assert response.body['student']['name'] == repo.students[4].name
        assert response.body['message'] == "the selfies were retriven"

    def test_get_selfies_by_ra_controller_invalid_ra_int(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesByRaUsecase(repo=repo)
        controller = GetSelfiesByRaController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": 21010757,
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "ra must be a string"
        
    def test_get_selfies_by_ra_controller_not_found_ra(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesByRaUsecase(repo=repo)
        controller = GetSelfiesByRaController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "21002081",
        })

        response = controller(request=request)

        assert response.status_code == 404
        assert response.body == "No items found for ra"
        
    def test_get_selfies_by_ra_controller_missing_ra(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesByRaUsecase(repo=repo)
        controller = GetSelfiesByRaController(usecase=usecase)

        request = HttpRequest(query_params={
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field ra is missing"
    
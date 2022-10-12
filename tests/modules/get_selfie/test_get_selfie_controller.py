from src.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound
from src.modules.get_selfie.get_selfie_usecase import GetSelfieUsecase
from src.modules.get_selfie.get_selfie_controller import GetSelfieController

class Test_GetSelfieController:
    def test_get_selfie_controller(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfieUsecase(repo=repo)
        controller = GetSelfieController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": repo.students[0].ra,
            "idSelfie": repo.selfies[0].idSelfie
        })

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body['url'] == repo.selfies[0].url 
        assert response.body['dateUpload'] == repo.selfies[0].dateUpload.isoformat()  
        assert response.body['state'] == "DECLINED"
        assert response.body['message'] == "the selfie was retriven"
        
    # def test_get_selfie_controller_no_selfies(self):
    #     repo = StudentRepositoryMock()
    #     usecase = GetSelfiesUsecase(repo=repo)
    #     controller = GetSelfiesController(usecase=usecase)

    #     request = HttpRequest(query_params={
    #         "ra": repo.students[4].ra,
    #     })

    #     response = controller(request=request)

    #     assert response.status_code == 200
    #     assert len(response.body['selfies']) == 0
    #     assert response.body['student']['name'] == repo.students[4].name
    #     assert response.body['message'] == "the selfies were retriven"

    # def test_get_selfie_controller_invalid_ra_int(self):
    #     repo = StudentRepositoryMock()
    #     usecase = GetSelfiesUsecase(repo=repo)
    #     controller = GetSelfiesController(usecase=usecase)

    #     request = HttpRequest(query_params={
    #         "ra": 21010757,
    #     })

    #     response = controller(request=request)

    #     assert response.status_code == 400
    #     assert response.body == "ra must be a string"
        
    # def test_get_selfie_controller_not_found_ra(self):
    #     repo = StudentRepositoryMock()
    #     usecase = GetSelfiesUsecase(repo=repo)
    #     controller = GetSelfiesController(usecase=usecase)

    #     request = HttpRequest(query_params={
    #         "ra": "21002081",
    #     })

    #     response = controller(request=request)

    #     assert response.status_code == 404
    #     assert response.body == "No items found for ra"
        
    # def test_get_selfie_controller_missing_ra(self):
    #     repo = StudentRepositoryMock()
    #     usecase = GetSelfiesUsecase(repo=repo)
    #     controller = GetSelfiesController(usecase=usecase)

    #     request = HttpRequest(query_params={
    #     })

    #     response = controller(request=request)

    #     assert response.status_code == 400
    #     assert response.body == "Field ra is missing"
    
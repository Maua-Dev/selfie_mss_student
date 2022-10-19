from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.http.http_models import HttpRequest
from src.modules.get_selfie.app.get_selfie_usecase import GetSelfieUsecase
from src.modules.get_selfie.app.get_selfie_controller import GetSelfieController

class Test_GetSelfieController:
    def test_get_selfie_controller(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfieUsecase(repo=repo)
        controller = GetSelfieController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": repo.students[0].ra,
            "idSelfie": '0'
        })

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body['url'] == repo.selfies[0].url 
        assert response.body['dateUpload'] == repo.selfies[0].dateUpload.isoformat()  
        assert response.body['state'] == "DECLINED"
        assert response.body['rejectionReason'] == "COVERED_FACE"
        assert response.body['rejectionDescription'] == "Balaclava"
        assert response.body['message'] == "the selfie was retriven"
        
    def test_get_selfie_controller_no_selfie(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfieUsecase(repo=repo)
        controller = GetSelfieController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": repo.students[4].ra,
            "idSelfie": '10'
            
        })

        response = controller(request=request)

        assert response.status_code == 404

    def test_get_selfie_controller_invalid_ra_int(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfieUsecase(repo=repo)
        controller = GetSelfieController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": 21010757,
            "idSelfie": '1000000'
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "ra must be a string"
    
    def test_get_selfie_controller_invalid_id_not_int(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfieUsecase(repo=repo)
        controller = GetSelfieController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "21010757",
            "idSelfie": "Guardanapo"
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field idSelfie is not valid"
    
    def test_get_selfie_controller_invalid_id_not_decimal(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfieUsecase(repo=repo)
        controller = GetSelfieController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "21010757",
            "idSelfie": "Guardanas"
        })

        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field idSelfie is not valid"
    
    def test_get_selfie_controller_invalid_id_str(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfieUsecase(repo=repo)
        controller = GetSelfieController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "21010757",
            "idSelfie": 1
        })

        
        
        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field idSelfie isn\'t in the right type.\n Received: int.\n Expected: str"
        

    def test_get_selfie_controller_not_found_ra(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfieUsecase(repo=repo)
        controller = GetSelfieController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "21002081",
            "idSelfie": '40028922'
        })

        response = controller(request=request)

        assert response.status_code == 404
        assert response.body == "No items found for ra or idSelfie"
        
    def test_get_selfie_controller_missing_ra(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfieUsecase(repo=repo)
        controller = GetSelfieController(usecase=usecase)

        request = HttpRequest(query_params={
            "idSelfie": '40028922'
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field ra is missing"
    
       
    def test_get_selfie_controller_missing_id(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfieUsecase(repo=repo)
        controller = GetSelfieController(usecase=usecase)

        request = HttpRequest(query_params={
             "ra": "21002081",
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field idSelfie is missing"
    
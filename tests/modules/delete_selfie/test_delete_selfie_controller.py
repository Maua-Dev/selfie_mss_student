import pytest
from src.domain.entities.student import Student
from src.helpers.errors.domain_errors import EntityError
from src.modules.delete_selfie.delete_selfie_controller import DeleteSelfieController
from src.modules.delete_selfie.delete_selfie_usecase import DeleteSelfieUsecase
from src.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound

class Test_DeleteSelfieController:

    def test_delete_selfie_controller(self):
        repo = StudentRepositoryMock()
        lenghtBefore = len(repo.selfies)
        usecase = DeleteSelfieUsecase(repo=repo)
        controller = DeleteSelfieController(usecase=usecase)
        request = HttpRequest(query_params={
            "ra": "21010757",
            "idSelfie": "0"
        })
        response = controller(request=request)

        expected = {
            'student':{
            "ra":"21010757",
   "name":"Victor",
            "email":"eusousoller@gmail.com"
        },
            'selfie':{
 'dateUpload': '2022-10-12T16:01:59.149927',
            'idSelfie': 0,
            'state': 'DECLINED',
            'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
            },
            'message':"the selfie was deleted"
          }
        
        assert response.status_code == 200
        assert len(repo.selfies) == lenghtBefore - 1
        assert response.body == expected

    def test_delete_selfie_controller_selfie_not_found(self):
        repo = StudentRepositoryMock()
        lenghtBefore = len(repo.selfies)
        usecase = DeleteSelfieUsecase(repo=repo)
        controller = DeleteSelfieController(usecase=usecase)
        request = HttpRequest(query_params={
            "ra": "21010757",
            "idSelfie": "10"
        })
        response = controller(request=request)

        expected = {
            'student':{
            "ra":"21010757",
   "name":"Victor",
            "email":"eusousoller@gmail.com"
        },
            'selfie':{
 'dateUpload': '2022-10-12T16:01:59.149927',
            'idSelfie': 0,
            'state': 'DECLINED',
            'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
            },
            'message':"the selfie was deleted"
          }
        
        assert response.body == "No items found for ra or idSelfie"
        assert response.status_code == 404


    def test_delete_selfie_controller_no_ra_found(self):
        repo = StudentRepositoryMock()
        usecase = DeleteSelfieUsecase(repo=repo)
        controller = DeleteSelfieController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "21007586",
            "idSelfie": "10"
        })

        response = controller(request=request)

        assert response.body == "No items found for ra or idSelfie"
        assert response.status_code == 404

    def test_delete_selfie_controller_bad_request_missing_ra(self):
        repo = StudentRepositoryMock()
        usecase = DeleteSelfieUsecase(repo=repo)
        controller = DeleteSelfieController(usecase=usecase)

        request = HttpRequest(query_params={
            "idSelfie": "10"
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field ra is missing"


    def test_delete_selfie_controller_bad_request_missing_idSelfie(self):
        repo = StudentRepositoryMock()
        usecase = DeleteSelfieUsecase(repo=repo)
        controller = DeleteSelfieController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "21007586",
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field idSelfie is missing"

    def test_delete_selfie_controller_bad_request_ra_int(self):
        repo = StudentRepositoryMock()
        usecase = DeleteSelfieUsecase(repo=repo)
        controller = DeleteSelfieController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": 21014440,
            "idSelfie": "1"
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "ra must be a string"

    def test_delete_selfie_controller_bad_request_invalid_ra(self):
        repo = StudentRepositoryMock()
        usecase = DeleteSelfieUsecase(repo=repo)
        controller = DeleteSelfieController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "2101444",
            "idSelfie": "10"
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field ra is not valid"

    def test_delete_selfie_controller_bad_request_Idselfie_int(self):
          repo = StudentRepositoryMock()
          usecase = DeleteSelfieUsecase(repo=repo)
          controller = DeleteSelfieController(usecase=usecase)

          request = HttpRequest(query_params={
              "ra": "21010757",
              "idSelfie": 1
          })

          response = controller(request=request)

          assert response.status_code == 400
          assert response.body == "Field idSelfie isn\'t in the right type.\nReceived: int\nExpected: str"

    def test_delete_selfie_controller_bad_request_Idselfie_word(self):
        repo = StudentRepositoryMock()
        usecase = DeleteSelfieUsecase(repo=repo)
        controller = DeleteSelfieController(usecase=usecase)

        request = HttpRequest(query_params= {
            "ra": "21010757",
            "idSelfie": "MACACOUAUAUAUAUAUAAUAUAU"
        })

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field idSelfie is not valid"


      
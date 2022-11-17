
import pytest
from src.modules.request_upload_selfie.app.request_upload_selfie_controller import RequestUploadSelfieController
from src.modules.request_upload_selfie.app.request_upload_selfie_usecase import RequestUploadSelfieUsecase
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.http.http_models import HttpRequest
from src.shared.infra.repositories.selfie_repository_mock import SelfieRepositoryMock
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock


class Test_RequestUploadSelfieController:

    def test_request_upload_selfie_controller(self):
        repoSelfie = SelfieRepositoryMock()
        repoStudent = StudentRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repoSelfie=repoSelfie, repoStudent=repoStudent)
        controller = RequestUploadSelfieController(usecase=usecase)
        request = HttpRequest(body={
            "ra": "21002088",
            "name": "MARIA LUIZA VERNASQUI VERGANI",
            "email": "21.00208-8@maua.br",
        })
        
        response = controller(request=request)
        
        assert response.body["url"] == "https://test-selfie-bucket.s3.amazonaws.com/"
        assert response.body["fields"]['x-amz-meta-ra'] == "21002088"
        assert response.body["fields"]['x-amz-meta-name'] == "MARIA LUIZA VERNASQUI VERGANI"
        assert response.body["fields"]['x-amz-meta-email'] == "21.00208-8@maua.br"
        assert '21002088' in response.body["fields"]['key']
        assert response.body["fields"]['AWSAccessKeyId'] == "ACCESSKEY-21002088"
        assert response.body["fields"]['policy'] == "POLICY-21002088"
        assert response.body["fields"]['signature'] == "SIGNATURE-21002088"
       

    def test_request_upload_selfie_missing_ra(self):
        repoSelfie = SelfieRepositoryMock()
        repoStudent = StudentRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repoSelfie=repoSelfie, repoStudent=repoStudent)
        controller = RequestUploadSelfieController(usecase=usecase)
        request = HttpRequest(body={
            "email": "21.00208-8@maua.br",
            "name": "MARIA LUIZA VERNASQUI VERGANI",
        })
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field ra is missing"

    def test_request_upload_selfie_missing_email(self):
        repoSelfie = SelfieRepositoryMock()
        repoStudent = StudentRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repoSelfie=repoSelfie, repoStudent=repoStudent)
        controller = RequestUploadSelfieController(usecase=usecase)
        request = HttpRequest(body={
            "ra": "21002088",
            "name": "MARIA LUIZA VERNASQUI VERGANI",
        })
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field email is missing"

    def test_request_upload_selfie_missing_name(self):
        repoSelfie = SelfieRepositoryMock()
        repoStudent = StudentRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repoSelfie=repoSelfie, repoStudent=repoStudent)
        controller = RequestUploadSelfieController(usecase=usecase)
        request = HttpRequest(body={
            "ra": "21002088",
            "email": "21.00208-8@maua.br",
        })
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field name is missing"

    def test_request_upload_selfie_error_ra(self):
        repoSelfie = SelfieRepositoryMock()
        repoStudent = StudentRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repoSelfie=repoSelfie, repoStudent=repoStudent)
        controller = RequestUploadSelfieController(usecase=usecase)
        request = HttpRequest(body={
            "ra": "2100208-8",
            "name": "MARIA LUIZA VERNASQUI VERGANI",
            "email": "21.00208-8@maua.br",
        })
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field ra is not valid"

    def test_request_upload_selfie_error_name(self):
        repoSelfie = SelfieRepositoryMock()
        repoStudent = StudentRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repoSelfie=repoSelfie, repoStudent=repoStudent)
        controller = RequestUploadSelfieController(usecase=usecase)
        request = HttpRequest(body={
            "ra": "21002088",
            "name": "M",
            "email": "21.00208-8@maua.br",
        })
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field name is not valid"

    def test_request_upload_selfie_error_email(self):
        repoSelfie = SelfieRepositoryMock()
        repoStudent = StudentRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repoSelfie=repoSelfie, repoStudent=repoStudent)
        controller = RequestUploadSelfieController(usecase=usecase)
        request = HttpRequest(body={
            "ra": "21002088",
            "name": "MARIA LUIZA VERNASQUI VERGANI",
            "email": "21.00208-8@mauabr",
        })
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field email is not valid"

    def test_request_upload_selfie_selfie_approved(self):
        repoSelfie = SelfieRepositoryMock()
        repoStudent = StudentRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repoSelfie=repoSelfie, repoStudent=repoStudent)
        controller = RequestUploadSelfieController(usecase=usecase)
        request = HttpRequest(body={
            "ra": "15013103",
            "name": "HECTOR GUERRINI HERRERA",
            "email": "15.01310-3@gmail.com",
        })
        response = controller(request=request)

        assert response.status_code == 403
        assert response.body == 'That action is forbidden for this Student'

    def test_request_upload_selfie_selfie_in_review(self):
        repoSelfie = SelfieRepositoryMock()
        repoStudent = StudentRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repoSelfie=repoSelfie, repoStudent=repoStudent)
        controller = RequestUploadSelfieController(usecase=usecase)
        request = HttpRequest(body={
            "ra": "21014442",
            "name": "VITOR GUIRAO SOLLER",
            "email": "21.01444-2@gmail.com",
        })
        response = controller(request=request)

        assert response.status_code == 403
        assert response.body == 'That action is forbidden for this Student'
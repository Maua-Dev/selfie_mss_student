
import pytest
from src.modules.request_upload_selfie.app.request_upload_selfie_controller import RequestUploadSelfieController
from src.modules.request_upload_selfie.app.request_upload_selfie_usecase import RequestUploadSelfieUsecase
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.http.http_models import HttpRequest
from src.shared.infra.repositories.selfie_repository_mock import SelfieRepositoryMock


class Test_RequestUploadSelfieController:

    def test_request_upload_selfie_controller(self):
        repo = SelfieRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repo=repo)
        controller = RequestUploadSelfieController(usecase=usecase)
        request = HttpRequest(body={
            "ra": "21014442",
            "name": "VITOR GUIRAO SOLLER",
            "email": "21.01444-2@maua.br",
        })
        
        response = controller(request=request)
        
        assert response.body["url"] == "https://test-selfie-bucket.s3.amazonaws.com/"
        assert response.body["fields"]['x-amz-meta-ra'] == "21014442"
        assert response.body["fields"]['x-amz-meta-name'] == "VITOR GUIRAO SOLLER"
        assert response.body["fields"]['x-amz-meta-email'] == "21.01444-2@maua.br"
        assert '21014442' in response.body["fields"]['key']
        assert response.body["fields"]['AWSAccessKeyId'] == "ACCESSKEY-21014442"
        assert response.body["fields"]['policy'] == "POLICY-21014442"
        assert response.body["fields"]['signature'] == "SIGNATURE-21014442"
       

    def test_request_upload_selfie_missing_ra(self):
        repo = SelfieRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repo=repo)
        controller = RequestUploadSelfieController(usecase=usecase)
        request = HttpRequest(body={
            "name": "VITOR GUIRAO SOLLER",
            "email": "21.01444-2@maua.br"
        })
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field ra is missing"

    def test_request_upload_selfie_missing_email(self):
        repo = SelfieRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repo=repo)
        controller = RequestUploadSelfieController(usecase=usecase)
        request = HttpRequest(body={
            "ra": "21014442",
            "name": "VITOR GUIRAO SOLLER"
        })
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field email is missing"

    def test_request_upload_selfie_missing_name(self):
        repo = SelfieRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repo=repo)
        controller = RequestUploadSelfieController(usecase=usecase)
        request = HttpRequest(body={
            "ra": "21014442",
            "email": "21.01444-2@maua.br"
        })
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field name is missing"

    def test_request_upload_selfie_error_ra(self):
        repo = SelfieRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repo=repo)
        controller = RequestUploadSelfieController(usecase=usecase)
        request = HttpRequest(body={
            "ra": "2101444-2",
            "name": "VITOR GUIRAO SOLLER",
            "email": "21.01444-2@maua.br"
        })
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field ra is not valid"

    def test_request_upload_selfie_error_name(self):
        repo = SelfieRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repo=repo)
        controller = RequestUploadSelfieController(usecase=usecase)
        request = HttpRequest(body={
            "ra": "21014442",
            "name": "V",
            "email": "21.01444-2@maua.br"
        })
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field name is not valid"

    def test_request_upload_selfie_error_email(self):
        repo = SelfieRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repo=repo)
        controller = RequestUploadSelfieController(usecase=usecase)
        request = HttpRequest(body={
            "ra": "21014442",
            "name": "VITOR GUIRAO SOLLER",
            "email": "21.01444-2@mauabr"
        })
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field email is not valid"

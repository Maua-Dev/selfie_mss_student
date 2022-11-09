from src.modules.request_upload_selfie.app.request_upload_selfie_usecase import RequestUploadSelfieUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
import pytest
from src.shared.infra.repositories.selfie_repository_mock import SelfieRepositoryMock

class Test_RequestUploadSelfieUsecase:
    def test_request_upload_selfie(self):
        repo = SelfieRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repo=repo)
       
        presignedPost = usecase(ra="21014442", name="VITOR GUIRAO SOLLER", email="21.01444-2@gmail.com")
       
        assert presignedPost['url'] == "https://test-selfie-bucket.s3.amazonaws.com/"
        assert presignedPost['fields']['x-amz-meta-ra'] == "21014442"
        assert presignedPost['fields']['x-amz-meta-name'] == "VITOR GUIRAO SOLLER"
        assert presignedPost['fields']['x-amz-meta-email'] == "21.01444-2@gmail.com"
        assert '21014442' in presignedPost['fields']['key']
        assert presignedPost['fields']['AWSAccessKeyId'] == "ACCESSKEY-21014442"
        assert presignedPost['fields']['policy'] == "POLICY-21014442"
        assert presignedPost['fields']['signature'] == "SIGNATURE-21014442"
 
    def test_request_upload_selfie_error_ra(self):
        repo = SelfieRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repo=repo)
       
        with pytest.raises(EntityError):
            presignedPost = usecase(ra="2101444-2", name="VITOR GUIRAO SOLLER", email="21.01444-2@gmail.com")
       
    def test_request_upload_selfie_error_email(self):
        repo = SelfieRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repo=repo)
       
        with pytest.raises(EntityError):
            presignedPost = usecase(ra="21014442", name="VITOR GUIRAO SOLLER", email="21.01444-2gmail.com")

        
    def test_request_upload_selfie_error_name(self):
        repo = SelfieRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repo=repo)
       
        with pytest.raises(EntityError):
            presignedPost = usecase(ra="21014442", name="V", email="21.01444-2@gmail.com")


       
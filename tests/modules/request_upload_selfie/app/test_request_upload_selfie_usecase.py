from src.modules.request_upload_selfie.app.request_upload_selfie_usecase import RequestUploadSelfieUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
import pytest
from src.shared.infra.repositories.selfie_repository_mock import SelfieRepositoryMock
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock

class Test_RequestUploadSelfieUsecase:
    def test_request_upload_selfie(self):
        repoSelfie = SelfieRepositoryMock()
        repoStudent = StudentRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repoSelfie=repoSelfie, repoStudent=repoStudent)
       
        presignedPost = usecase(ra="21002088", name="MARIA LUIZA VERNASQUI VERGANI", email="21.00208-8@maua.br")
       

        assert presignedPost['url'] == "https://test-selfie-bucket.s3.amazonaws.com/"
        assert presignedPost['fields']['x-amz-meta-ra'] == "21002088"
        assert presignedPost['fields']['x-amz-meta-name'] == "MARIA LUIZA VERNASQUI VERGANI"
        assert presignedPost['fields']['x-amz-meta-email'] == "21.00208-8@maua.br"
        assert '21002088' in presignedPost['fields']['key']
        assert presignedPost['fields']['AWSAccessKeyId'] == "ACCESSKEY-21002088"
        assert presignedPost['fields']['policy'] == "POLICY-21002088"
        assert presignedPost['fields']['signature'] == "SIGNATURE-21002088"
 
    def test_request_upload_selfie_error_ra(self):
        repoSelfie = SelfieRepositoryMock()
        repoStudent = StudentRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repoSelfie=repoSelfie, repoStudent=repoStudent)
       
        with pytest.raises(EntityError):
            presignedPost = usecase(ra="2100208-8", name="MARIA LUIZA VERNASQUI VERGANI", email="21.00208-8@maua.br")
       
    def test_request_upload_selfie_error_email(self):
        repoSelfie = SelfieRepositoryMock()
        repoStudent = StudentRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repoSelfie=repoSelfie, repoStudent=repoStudent)
       
        with pytest.raises(EntityError):
            presignedPost = usecase(ra="21002088", name="MARIA LUIZA VERNASQUI VERGANI", email="21.00208-8maua.br")

        
    def test_request_upload_selfie_error_name(self):
        repoSelfie = SelfieRepositoryMock()
        repoStudent = StudentRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repoSelfie=repoSelfie, repoStudent=repoStudent)
       
        with pytest.raises(EntityError):
            presignedPost = usecase(ra="21002088", name="M", email="21.00208-8@maua.br")


        
    def test_request_upload_selfie_selfie_approved(self):
        repoSelfie = SelfieRepositoryMock()
        repoStudent = StudentRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repoSelfie=repoSelfie, repoStudent=repoStudent)
       
        with pytest.raises(ForbiddenAction):
            presignedPost = usecase(ra="15013103", name="HECTOR GUERRINI HERRERA", email="15.01310-3@maua.com")
       
        
    def test_request_upload_selfie_selfie_in_review(self):
        repoSelfie = SelfieRepositoryMock()
        repoStudent = StudentRepositoryMock()
        usecase = RequestUploadSelfieUsecase(repoSelfie=repoSelfie, repoStudent=repoStudent)
       
        with pytest.raises(ForbiddenAction):
            presignedPost = usecase(ra="21014442", name="VITOR GUIRAO SOLLER", email="21.01444-2@maua.com")


       
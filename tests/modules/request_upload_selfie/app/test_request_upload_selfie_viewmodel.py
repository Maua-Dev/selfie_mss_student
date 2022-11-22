from src.modules.request_upload_selfie.app.request_upload_selfie_viewmodel import RequestUploadSelfieViewModel
from src.shared.infra.repositories.selfie_repository_mock import SelfieRepositoryMock

class Test_RequestUploadSelfieViewModel:
    def test_request_upload_selfie_viewmodel(self):
        repo = SelfieRepositoryMock()
  
        presignedPostDict = {
        "url":"https://test-selfie-bucket.s3.amazonaws.com/",
        "metadata":{
            "ra":"21014442",
            "name":"VITOR GUIRAO SOLLER",
            "email":"21.01444-2@gmail.com"
   }
}

        presignedPostViewModel = RequestUploadSelfieViewModel(presignedPost=presignedPostDict).to_dict()


        expected = {
          "url":"https://test-selfie-bucket.s3.amazonaws.com/",
          "fields":{
              "x-amz-meta-ra":"21014442",
              "x-amz-meta-name":"VITOR GUIRAO SOLLER",
              "x-amz-meta-email":"21.01444-2@gmail.com",
          }
        }
        
        assert presignedPostViewModel == expected
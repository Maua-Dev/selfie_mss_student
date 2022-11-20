from src.shared.environments import Environments
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from .request_upload_selfie_controller import RequestUploadSelfieController
from .request_upload_selfie_usecase import RequestUploadSelfieUsecase
from src.shared.helpers.http.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.shared.infra.repositories.selfie_repository_mock import SelfieRepositoryMock


def lambda_handler(event, context):
    repoSelfie = Environments.get_selfie_repo()()
    repoStudent = Environments.get_student_repo()()
    usecase = RequestUploadSelfieUsecase(repoSelfie=repoSelfie, repoStudent=repoStudent)
    controller = RequestUploadSelfieController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    print(response)
    httpResponse = LambdaHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.headers)
    print(httpResponse)

    return httpResponse.toDict()
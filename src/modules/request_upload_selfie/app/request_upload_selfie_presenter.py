from .request_upload_selfie_controller import RequestUploadSelfieController
from .request_upload_selfie_usecase import RequestUploadSelfieUsecase
from src.shared.helpers.http.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.shared.infra.repositories.selfie_repository_mock import SelfieRepositoryMock


def lambda_handler(event, context):
    repo = SelfieRepositoryMock()
    usecase = RequestUploadSelfieUsecase(repo)
    controller = RequestUploadSelfieController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
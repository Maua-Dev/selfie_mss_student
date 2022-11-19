from src.shared.environments import Environments
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.http.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from .get_selfie_controller import GetSelfieController
from .get_selfie_usecase import GetSelfieUsecase



def lambda_handler(event, context):
    repo = Environments.get_student_repo()()
    usecase = GetSelfieUsecase(repo)
    controller = GetSelfieController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()


from src.shared.environments import Environments
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.http.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from .reject_selfie_controller import RejectSelfieController
from .reject_selfie_usecase import RejectSelfieUsecase



def lambda_handler(event, context):
    repo = Environments.get_student_repo()()
    usecase = RejectSelfieUsecase(repo)
    controller = RejectSelfieController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()


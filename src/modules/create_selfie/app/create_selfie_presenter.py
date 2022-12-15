from src.shared.environments import Environments
from .create_selfie_usecase import CreateSelfieUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from .create_selfie_controller import CreateSelfieController
from src.shared.helpers.http.http_lambda_requests import LambdaHttpResponse
from src.shared.helpers.http.http_models import HttpRequest

repo = Environments.get_student_repo()()
usecase = CreateSelfieUsecase(repo)
controller = CreateSelfieController(usecase)


def lambda_handler(event: dict, context):
    http_request = HttpRequest(body=event, headers=event.get("headers"), query_params=event.get("query_params"))

    response = controller(request=http_request)
    httpResponse = LambdaHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

from src.shared.environments import Environments
from .get_all_selfies_controller import GetAllSelfiesController
from .get_all_selfies_usecase import GetAllSelfiesUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.http.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse



def lambda_handler(event, context):
    repo = Environments.get_student_repo()()
    usecase = GetAllSelfiesUsecase(repo)
    controller = GetAllSelfiesController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()


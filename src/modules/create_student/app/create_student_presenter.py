from src.shared.environments import Environments
from .create_student_usecase import CreateStudentUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from .create_student_controller import CreateStudentController
from src.shared.helpers.http.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse


def lambda_handler(event, context):
    repo = Environments.get_student_repo()()
    usecase = CreateStudentUsecase(repo)
    controller = CreateStudentController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
